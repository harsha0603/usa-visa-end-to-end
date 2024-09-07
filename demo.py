from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
logging.info("Testing logging code successfull")


try:
    a = 7/0
except Exception as e:
    raise USvisaException(e,sys)