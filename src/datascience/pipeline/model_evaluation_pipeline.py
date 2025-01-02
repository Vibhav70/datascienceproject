from src.datascience.configs.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluation_pipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation1 = ModelEvaluation(config=model_evaluation_config)
        model_evaluation1.log_into_mlfow()