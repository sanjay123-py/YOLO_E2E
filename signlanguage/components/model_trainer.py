import os, sys
import shutil
import yaml
from signlanguage.utils.main_utils import read_yaml_file
from signlanguage.logger import logging
from signlanguage.exception import SignException
from signlanguage.entity.config_entity import ModelTrainerConfig
from signlanguage.entity.artifact_entity import ModelTrainerArtifact, DataValidationArtifact

class ModelTrainer:
    def __init__(self,
                 model_trainer_config = ModelTrainerConfig
                 ):
        self.model_trainer_config=model_trainer_config
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate modelt trainer of modeltrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip Sign_language_data.zip")
            os.system('rm Sign_language_data.zip')
            with open("data.yaml",'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)
            config = read_yaml_file(f'./yolov5/models/{model_config_file_name}.yaml')
            config['nc']=int(num_classes)
            with open(f'./yolov5/models/custom_{model_config_file_name}.yaml','w') as f:
                yaml.dump(config,f)
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_trainer_dir,exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt"
            )
            logging.info('Exited initiate_model_trainer method of Mode trainer class')
            logging.info(f"Model trinaer artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise SignException(e,sys)
