import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and returns
    
    Args:
        path_to_yaml: Path to yaml file
    Raises:
        ValueError: If yaml is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox object
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"Read yaml file from {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f"Empty file")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """Create a list of directories

    Args:
        path_to_directories (list): _description_
        ignore_log(bool,optional): ignore if multiple directories are created
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at: {path}')


@ensure_annotations
def save_json(path_to_save:Path, data:dict):
    """Save json file

    Args:
        path_to_save (Path): Path to save json file
        data (dict): data to save
    """
    with open(path_to_save, "w") as f:
        json.dump(data, f,indent=4)
    
    logger.info(f"json fike saved at {path_to_save}")
    
@ensure_annotations
def load_json(path_to_load:Path)-> ConfigBox:
    """Load json file

    Args:
        path_to_load (Path): Path to load json file

    Returns:
        ConfigBox: ConfigBox object
    """
    with open(path_to_load) as f:
        content=json.load(f)
        
    logger.info(f"json file loaded from: {path_to_load}")
    return ConfigBox(content)

@ensure_annotations
def save_pickle(path_to_save:Path, data:Any):
    """Save pickle file

    Args:
        path_to_save (Path): Path to save pickle file
        data (Any): data to save
    """
    joblib.dump(value=data, filename=path_to_save)
    

@ensure_annotations
def load_pickle(path_to_load:Path)-> Any:
    """load pickle file
    
    Args:
        path_to_load (Path): Path to load pickle file
    
    Returns:
        Any: data loaded from pickle file
    """
    
    data=joblib.load(path_to_load)
    
    logger.info(f"pickle file loaded from: {path_to_load}")
    return data


@ensure_annotations
def get_size(path:Path)->str:
    """Get size of file

    Args:
        path (Path): Path to file
    
    Returns:
        str: size of file
    """
    
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
    

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    