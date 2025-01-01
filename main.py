from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>{STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>{STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e