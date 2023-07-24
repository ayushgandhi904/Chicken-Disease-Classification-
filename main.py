from chicken_classifier import logger
from chicken_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"----------{STAGE_NAME} started ----------")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"----------{STAGE_NAME} completed----------")
except Exception as e:
    logger.exception(e)
    raise e