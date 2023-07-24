from chicken_classifier.config.configuration import ConfigurationManager
from chicken_classifier.components.data_ingestion import DataIngstion
from chicken_classifier import logger



STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngstion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        


if __name__ == "__main__":
    try:
        logger.info(f"----------{STAGE_NAME} started ----------")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"----------{STAGE_NAME} completed----------")
    except Exception as e:
        logger.exception(e)
        raise e