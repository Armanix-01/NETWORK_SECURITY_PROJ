import os
import sys
import numpy as np
import pandas as pd

##Data ingestion related constant starts with DATA_INGESTION
# VAR NAME

DATA_INGESTION_COLLECTION_NAME:str= 'NetworkData'
DATA_INGESTION_DATABASE_NAME:str = "ARMANIX_PROJ"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

##Defining common constant variable for training variable
TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "NetworkData.csv"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
