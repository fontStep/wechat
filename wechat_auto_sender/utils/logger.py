import logging
from logging.handlers import TimedRotatingFileHandler

class LoggerHelper:
    @staticmethod
    def get_logger(log_file='wechat_sender.log', level=logging.INFO):
        logger = logging.getLogger(log_file)
        logger.setLevel(level)
        if not logger.handlers:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler = TimedRotatingFileHandler(log_file, when='midnight', backupCount=7, encoding='utf-8')
            file_handler.setFormatter(formatter)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)
        return logger 