
from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_transformation import DataTransformation
from src.DataScienceProject import logger


try:
    config=ConfigurationManager()
    data_transformation_config =config.get_data_transformation_config()
    data_transformation= DataTransformation(config=data_transformation_config)
    data_transformation.train_test_splitting()
except Exception as e:
    raise e

STAGE_NAME ="Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()
       # data_validation.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj =DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n x==========x")
    except Exception as e:
        logger.exception(e)
        raise e