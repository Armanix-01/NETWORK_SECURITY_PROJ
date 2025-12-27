import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constant import training_pipeline
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataValidataionConfig, DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file
from scipy.stats import ks_2samp
import pandas as pd

schema = read_yaml_file(SCHEMA_FILE_PATH)
print(schema)
print(len(schema["columns"]))