#debug, info, warning, error, critical

import logging

logging.basicConfig(filename="C://Users//bobbu.yaswanth//Desktop//test.log",
                    format='%(asctime)s: %(levelname)s : %(message)s',datefmt = '%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

logging.debug("This is debug message")
logging.info("This is info message")
#threshold level
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

