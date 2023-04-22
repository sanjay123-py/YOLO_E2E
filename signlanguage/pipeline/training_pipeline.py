import os
import sys
from signlanguage.exception import SignException
from signlanguage.logger import logging
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.components.data_validation import DataValidation
from signlanguage.entity.config_entity import DataIngestionConfig, DataValidationConfig
from signlanguage.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

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
        logging.info("Getting the data from url")
        try:
            data_validation = DataValidation(data_ingestion_artifact, self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
            )
        except Exception as e:
            raise SignException(e, sys)