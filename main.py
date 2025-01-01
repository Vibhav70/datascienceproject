from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>{STAGE_NAME} completed <<<<<<<<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx=================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation = ModelTrainerPipeline()
    data_transformation.initiate_model_trainer()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx=================x")
except Exception as e:
        logger.exception(e)
        raise e