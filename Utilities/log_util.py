import logging
import os
import time

class Logger():
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        cwd = os.getcwd()

        format = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - %(levelname)s - %(message)s')
        current_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        if cwd =="D:\\Programming\\PythonProgramming\\PageObjectModelFramework":
            self.log_file_name = f"Logs\\log_{current_time}.log"
        else:
            self.log_file_name = f"..\\Logs\\log_{current_time}.log"
        file_handler = logging.FileHandler(self.log_file_name, mode="a")
        file_handler.setLevel(file_level)
        file_handler.setFormatter(format)
        self.logger.addHandler(file_handler)
