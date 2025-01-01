from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>{STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
