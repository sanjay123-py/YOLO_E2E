import os
import sys
from signlanguage.exception import SignException
from signlanguage.logger import logging
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.components.data_validation import DataValidation
from signlanguage.components.model_trainer import ModelTrainer
from signlanguage.components.model_pusher import ModelPusher
from signlanguage.entity.config_entity import DataIngestionConfig, DataValidationConfig, ModelTrainerConfig, ModelPusherConfig
from signlanguage.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact,ModelPusherArtifact
from signlanguage.configuration.s3_operations import S3Operation

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_pusher_config = ModelPusherConfig()
        self.s3_operations = S3Operation()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f"{'#'*10} Entered the data ingestion pipline {'#'*10}")
            logging.info("Getting the data from url")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Excited from data ingestion phase")
            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e,sys)

    def start_data_validation(self, data_ingestion_artifact:DataIngestionArtifact) -> DataValidationArtifact:
        logging.info(f"{'#'*10} Entered the data validation pipeline {'#'*10}")
        try:
            data_validation = DataValidation(data_ingestion_artifact, self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)
    def start_model_trainer(self, data_validation_artifact:DataValidationArtifact) -> ModelTrainerArtifact:
        logging.info(f"{'#'*10} Entered the Model trainer pipeline {'#'*10}")
        try:
            if(data_validation_artifact.validation_status==True):

                model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config)
                model_trainer_artifacts = model_trainer.initiate_model_trainer()
                return model_trainer_artifacts
            else:
                raise Exception("Wrong format of the data is been identified")
        except Exception as e:
            raise SignException(e, sys)
    def start_model_pusher(self,data_validation_artifact:DataValidationArtifact,model_trainer_artifact:ModelTrainerArtifact, s3:S3Operation):
        logging.info(f"{'#'*10} Entered the Model Pusher pipeline {'#'*10}")
        try:
            model_pusher = ModelPusher(
                model_pusher_config=self.model_pusher_config,
                model_trainer_artifact=model_trainer_artifact,
                s3=s3
            )
            if(data_validation_artifact.validation_status):
                model_pusher_artifact = model_pusher.initiate_model_pusher()
                return model_pusher_artifact
            else:
                raise Exception("Wrong format of the data is been identified")
        except Exception as e:
            raise SignException(e, sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )
            model_trainer_artifact = self.start_model_trainer(
                data_validation_artifact=data_validation_artifact
            )
            model_pusher_artifact = self.start_model_pusher(
                data_validation_artifact=data_validation_artifact,
                model_trainer_artifact=model_trainer_artifact,
                s3=self.s3_operations
            )
        except Exception as e:
            raise SignException(e, sys)

