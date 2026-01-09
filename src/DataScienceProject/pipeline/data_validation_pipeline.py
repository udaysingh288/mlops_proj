
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger


try:
    config=ConfigurationManager()
    data_validation_config =config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validate_all_columns()
except Exception as e:
    raise e

STAGE_NAME ="Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_validation(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
       # data_validation.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj =DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n x==========x")
    except Exception as e:
        logger.exception(e)
        raise e