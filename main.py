from MLProject import logger
from MLProject.pipeline.data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.data_validation import DataValidationTrainingPipeline
from MLProject.pipeline.data_transformation import DataTransformationTrainingPipeline
from MLProject.pipeline.model_trainer import ModelTrainerTrainingPipeline
from MLProject.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainning Stage"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>> Stage: {STAGE_NAME} STARTED <<<<<\n")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} COMPLETED <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e