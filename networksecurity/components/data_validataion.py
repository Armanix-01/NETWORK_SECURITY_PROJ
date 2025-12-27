import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constant import training_pipeline
from networksecurity.entity.config_entity import TrainingPipelineConfig, DataValidationConfig, DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd



class DataValidation:
    def __init__(self, daat_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = daat_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            df= pd.read_csv(file_path, header=0)
            df.reset_index(drop=True, inplace=True)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._schema_config['columns'])
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_columns:
                return True
            return False
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05 )->bool:
        try:
            status= True ## validation passed
            ##status tells is the data validation step 
            # successfull overall? Bascically we are checking
            # feature-wise drift, if any column has drift then
            # validation should fail
            
            report = {}
            for column in base_df.columns:
                d1 = base_df[column].dropna()
                d2 = current_df[column].dropna()
                is_same_dist = ks_2samp(d1,d2)
                if threshold<=is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False ##validation failed(drift exists)
                report.update({
                    column:{
                        "p_value":float(is_same_dist.pvalue),
                        "drift_status": is_found
                    }
                })
            
            
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            dir_path =os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)

            write_yaml_file(file_path=drift_report_file_path,
                            content=report)
            return status


                
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            ##Reading the data from train and test file path
            train_df = DataValidation.read_data(train_file_path)
            test_df = DataValidation.read_data(test_file_path)
            ##Validate number of columns
            status=self.validate_number_of_columns(dataframe=train_df)
            if not status:
                error_message= "Train dataframe didnt contain all the columns"
                raise NetworkSecurityException(f"{error_message}", sys)
            status =self.validate_number_of_columns(dataframe=test_df)
            if not status:
                error_message= "Test dataframe doesnt contain all the columns"
                raise NetworkSecurityException(f"{error_message}", sys)
       
            ##lets check datadrift
            status = self.detect_dataset_drift(base_df=train_df, current_df=test_df)
            dir_path_valid = os.path.dirname(self.data_validation_config.valid_test_file_dir)
            dir_path_invalid = os.path.dirname(self.data_validation_config.invalid_test_file_dir)
            os.makedirs(dir_path_invalid, exist_ok=True)
            os.makedirs(dir_path_valid, exist_ok=True)
            if status == False:
                self.data_validation_config.valid_train_file_dir = None
                self.data_validation_config.valid_test_file_dir = None
                train_df.to_csv(
                    self.data_validation_config.invalid_train_file_dir, index=False, header=True
                )
                test_df.to_csv(
                    self.data_validation_config.invalid_test_file_dir, index=False, header=True

                )
            else:
                self.data_validation_config.invalid_test_file_dir = None
                self.data_validation_config.invalid_train_file_dir = None
                train_df.to_csv(
                    self.data_validation_config.valid_train_file_dir, index=False, header=True
                )
                test_df.to_csv(
                    self.data_validation_config.valid_test_file_dir, index=False, header=True

                )

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_test_file_path= self.data_validation_config.valid_test_file_dir,
                valid_train_file_path= self.data_validation_config.valid_train_file_dir,
                invalid_train_file_path=  self.data_validation_config.invalid_train_file_dir,
                invalid_test_file_path= self.data_validation_config.invalid_test_file_dir,
                drift_report_file_path= self.data_validation_config.drift_report_file_path
            )
            return data_validation_artifact
            
        

            


        except Exception as e:
            raise NetworkSecurityException(e, sys)