import os
import urllib.request as request
import zipfile
from MLProject import logger
from MLProject.utils.common import get_size
from MLProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # function to download the data and save it into local directory
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} file has been downloaded having the info as: {headers}")
        else:
            logger.info(f"{filename} already exists of size (KB): {get_size(Path(self.config.local_data_file))}")

    # extracting the zip file
    def extract_zip_file(self):
        """
            zip_file_path: str
            Extract zip file into data directory
            Returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)