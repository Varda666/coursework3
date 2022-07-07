import logging
logger_one = logging.getLogger("one")
logger_one.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/logs.txt')
formatter_one = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
file_handler.setFormatter(formatter_one)
logger_one.addHandler(file_handler)

