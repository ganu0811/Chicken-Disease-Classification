from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_base_model import BaseModelPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Base Model Stage"

try:
    logger.info(f"********")
    logger.info(f">>>>> stage: {STAGE_NAME} started <<<<")
    base_model = BaseModelPipeline()
    base_model.main()
    logger.info(f">>>>> stage: {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e