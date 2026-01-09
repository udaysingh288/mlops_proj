import os
from src.DataScienceProject import logger
from src.DataScienceProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import pandas as pd



class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
        data= pd.read_csv(self.config.data_path)
        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Data split completed into train and test")
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Testing data shape:{test.shape}")

        print(train.shape)
        print(test.shape)
