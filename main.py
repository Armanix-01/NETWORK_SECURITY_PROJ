from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.components.data_validataion import DataValidation
import sys
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

if __name__=="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("data ingestion initiated")
        data_ingestion_artifact =data_ingestion.initiate_data_ingestion()
        logging.info("data initiated completed")
        data_validation_config = DataValidationConfig(training_pipeline_config)
        
        data_validation = DataValidation(daat_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)
        logging.info("initiate the date ingestion")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        logging.info("data transformation initiated")
        data_transformation_config = DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation = DataTransformation(
            data_validataion_artifact= data_validation_artifact,
            data_transformation_config=data_transformation_config
        )
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data transformation completed")
        logging.info("model trainer initiated")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config= model_trainer_config,
                                     data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        print(model_trainer_artifact)
        logging.info("model trainer ended")




    except Exception as e:
        raise NetworkSecurityException(e, sys)