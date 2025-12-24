import logging
import sys
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
##strftime (string format time) is a common function in
#  programming (Python, C/C++, SQL, PHP) that converts 
# date/time objects into human-readable strings, using 
# special codes like %Y (year) or %m (month) to define 
# the output format, offering precise control over how 
# dates and times are displayed
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level=logging.INFO
)


logging.info("checking if logging is working properly")