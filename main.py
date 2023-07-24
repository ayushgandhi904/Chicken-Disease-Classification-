from chicken_classifier import logger
from chicken_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"----------{STAGE_NAME} started ----------")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"----------{STAGE_NAME} completed----------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

if __name__ == "__main__":
    try:
        logger.info(f"----------{STAGE_NAME} started ----------")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"----------{STAGE_NAME} completed----------")
    except Exception as e:
        logger.exception(e)
        raise e