import logging
import os
import sys
from datetime import datetime
from from_root import from_root

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(from_root(),"log",LOG_FILE)
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
