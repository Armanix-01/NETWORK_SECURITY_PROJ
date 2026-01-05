import yaml
import os, sys
import dill
import pickle
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import dagshub
from dotenv import load_dotenv
load_dotenv()



def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def write_yaml_file(file_path:str, content:object, replace:bool = False)-> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


def save_numpy_array_data(file_path:str, array:np.array):
    """
    Here we are saving numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def save_object(file_path:str, obj:object)->None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    


def load_obj(file_path:str):
    try:
        with open(file_path, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def load_numpy_array_data(file_path:str) -> np.array:
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_path)
    except Exception as e:
        raise(e, sys)
    


def evaluate_models(x_train, y_train, x_test, y_test, models:dict, param:dict):
    try:
        report = {}

        for x in range(len(list(models))):
            model = list(models.values())[x]
            para = param[list(models.keys())[x]]
            gs = GridSearchCV(param_grid=para,
                              estimator=model, cv=3)
            gs.fit(x_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train, y_train)

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[x]]= test_model_score

            
        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)
    




_DAGSHUB_INITIALIZED = False

def setup_dagshub():
    global _DAGSHUB_INITIALIZED

    if _DAGSHUB_INITIALIZED:
        return

    if os.getenv("ENABLE_DAGSHUB", "false").lower() != "true":
        return

    token = os.getenv("DAGSHUB_TOKEN")
    if not token:
        raise RuntimeError("DAGSHUB_TOKEN not found")

    try:
        dagshub.auth.add_app_token(token=token)

        dagshub.init(
            repo_owner="armanixofficial01",
            repo_name="NETWORK_SECURITY_PROJ",
            mlflow=True
        )

        _DAGSHUB_INITIALIZED = True
        print("✅ DagsHub initialized successfully")

    except Exception as e:
        print("❌ Failed to initialize DagsHub:", e)
        raise


