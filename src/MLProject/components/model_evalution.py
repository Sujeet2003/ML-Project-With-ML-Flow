import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from MLProject.utils.common import save_json
from MLProject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, y_test, y_pred):
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        return rmse, mae, r2
    
    def login_to_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop(columns=['quality', 'Id'])
        y_test = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            y_pred = model.predict(X_test)
            rmse, mae, r2 = self.eval_metrics(y_test, y_pred)

            scores = {
                'rmse': rmse,
                'mae': mae,
                'r2_score': r2,
            }
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("RMSE", rmse)
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("R2 Score", r2)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")