import os

from time import sleep
from datetime import timedelta, datetime

import logging
logger = logging.getLogger(__name__)

import psycopg2
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    local_run = os.getenv('LOCAL_RUN',None)
    if  local_run:
        logging.basicConfig(
            filename='/logs/db_access.log',
            level=logging.INFO,
            format='%(asctime)s %(name)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(name)s %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.StreamHandler()
            ]            
        )

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="builty",
            user=os.getenv("DB_USER",''),
            password=os.getenv("DB_PASSWORD",'')
        )   
        logger.info("Connected to Builty DB")
    except Exception as ex:
        logger.error(str(ex))

    stop_point = datetime.now() + timedelta(minutes=5)

    while True:
        logger.info("Running")
        if datetime.now() > stop_point:
            break
        sleep(5)

    logger.info("Stopped")