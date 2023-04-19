import os
import sys
from signlanguage.exception import SignException
from signlanguage.logger import logging
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.entity.config_entity import DataIngestionConfig
from signlanguage.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

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
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e, sys)