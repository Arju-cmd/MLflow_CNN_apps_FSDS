import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories,unzip_file
import random
import urllib.request as req
from src.utils.datamanagement import validate_image

STAGE = "GET_DATA" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


#def main(config_path, params_path):
def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    print(config)
    URL = config['data']['source_url']
    local_dir = config['data']['local_dir']
    create_directories([local_dir]) 

    data_file = config['data']['data_file']
    data_file_path = os.path.join(local_dir, data_file)
    print("hello")

    if not os.path.isfile(data_file_path):
        logging.info("downloading started....")
        filename, headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename:{filename} created with info\n {headers}")
    else:
        logging.info(f"filename:{data_file} already present")

    #Unzip Ops
    unzip_data_dir = config['data']['unzip_data_dir']
    if not os.path.exists(unzip_data_dir):
        create_directories([unzip_data_dir])
        unzip_file(source=data_file_path, dest=unzip_data_dir)
    else:
        logging.info(f"data already extracted")
    # Validate data
    validate_image(config) 

if __name__ == '__main__':
    print("hello1")
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    #args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        print("hello2")
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        #main(config_path=parsed_args.config, params_path=parsed_args.params)
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e