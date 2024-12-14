import os
import yaml
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from MLProject import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ 
        Reads yaml file and returs ConfigBox type
        Args:
            path_to_yaml (str): path like input
        Raises:
            ValueError: if yaml file is empty
            e: empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        create a list of directories 
        Args:
            path_to_directories (list): list of path of directories
            verbose = True: print or log the detailed message
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")
        
@ensure_annotations
def save_json(path: Path, data: dict):
    """
        saves JSON data
        Args:
            path: Path to json file
            data (dict): data which has to be saved into json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
        load JSON files
        Args:
            path: path to json file
        Returns:
            ConfigBox: data as class attribute instead of dictionary
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
        save binary files
        Args:
            data (Any): any type of data to be saved as binary
            path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
        loads binary data
        Args:
            path (Path): path to load the binary file
        Returns:
            Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
        gets size in KB
        Args:
            path (Path): path of the file
        Returns:
            str: size of file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"