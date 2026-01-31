import os 
import yaml
import joblib
from src.datascience import logger
import json
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    """
    Reads Yaml and return 

    Args:
        path_to_yaml(str): path like input 
    
    Raises:
        ValueError : if yaml file is empty
        e: empty file
    
    Returns:
        configBox: configBox Type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is Empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose:True):
    """
    Create Lists of Directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool,optional): ignore if multiple dirs are created



    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created Directory at: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    """
    Docstring for save_json
    
    :param path: Description
    :type path: Path
    :param data: Description
    :type data: dict
    """

    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """
    Docstring for load_json
    
    :param path: Description
    :type path: Path
    :return: Description
    :rtype: ConfigBox
    """

    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    Docstring for save_bin
    
    :param data: Description
    :type data: Any
    :param path: Description
    :type path: Path
    """
    joblib.dump(value=data,filename=path)
    logger.info("Binary File Saved At this: {path}")

@ensure_annotations
def load_bin(path:Path)-> Any:
    """
    Docstring for load_bin
    
    :param path: Description
    :type path: Path
    :return: Description
    :rtype: Any
    """

    data = joblib.load(path)
    logger.info(f"Binary File Loaded from {path}")
    return data