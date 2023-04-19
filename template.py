import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name="signlanguage"
list_of_files=[
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/component/data_validation.py",
    f"{project_name}/component/model_trainer.py",
    f"{project_name}/component/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",

    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    "templates/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if(not os.path.exists(os.path.join(filedir,filename))):
        with open(os.path.join(filedir,filename) ,"w") as f: pass
        logging.info(f"Created a file: {filename} inside the directory: {filedir}")
    else:
        print("Files exist")


