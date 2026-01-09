from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
logger.info("Welcome to the custom test logger")


STAGE_NAME ="Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e

from src.DataScienceProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline


STAGE_NAME ="Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e

from src.DataScienceProject.pipeline.data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME ="Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e