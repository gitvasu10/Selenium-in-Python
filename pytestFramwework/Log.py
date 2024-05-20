import inspect
import logging
class Log:
    def log_function(self):
        loggerName = inspect.stack()[1][3] #This scans the stack trace to know which class has called the function
        logger = logging.getLogger(loggerName) #That function name will be passed into the logger
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
