import os
import yaml
from src.DataScienceProject import logger
import json
import joblib

from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """read yml file and returns"""

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded success")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
                        
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """creat list of directories
        
    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool,optional): ignore if multiple dirs is to created. Defaults to
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"create directory at:{path}")
             

@ensure_annotations
def save_json(path: Path, data: dict):
    """ save json dumps"""

    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path):
    """ save json dumps"""

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(path: Path, data: dict):
    """ save binary fie"""

    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def load_bin(path: Path):
    """ load  binary fie"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from :{path}")
    return data
