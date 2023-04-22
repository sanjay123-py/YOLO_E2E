import os

#Data Ingestion constants

ARTIFACTS_DIR: str = "artifacts"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"

#Data Validation constants

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yml"]

#model trainer constants
MODEL_TRAINER_DIR_NAME: str= "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME:str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 2
MODEL_TRAINER_BATCH_SIZE:int = 16
