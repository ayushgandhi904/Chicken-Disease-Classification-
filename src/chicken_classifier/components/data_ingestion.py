import os
import urllib.request as request
import zipfile
from chicken_classifier import logger
from chicken_classifier.utils.common import get_size
from chicken_classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngstion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    
    #downloading the data    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            
            logger.info(f"{filename} downloaded with info: \n{headers}")
            
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
    
    #unzipping the file
    def extract_zip_file(self):
        """
        Unzips the file which is availabele
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
            