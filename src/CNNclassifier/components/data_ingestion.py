import os
import zipfile
import gdown
from CNNclassifier import logger
from CNNclassifier.utils.common import get_size
from CNNclassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config

    

    def download_files(self)-> str:

        try:
            dataset_url= self.config.source_URL
            zip_download_dir= self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file")

        except Exception as e:
            raise e
    def extract_zip_files(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r')as zip_ref:
            zip_ref.extractall(unzip_path)
