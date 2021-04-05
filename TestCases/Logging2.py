#debug, info, warning, error, critical

import logging

logging.basicConfig(filename="C://Users//bobbu.yaswanth//Desktop//test2.log",
                    format='%(asctime)s: %(levelname)s : %(message)s',datefmt = '%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.debug("This is debug message")
logger.info("This is info message")
#threshold level
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")

