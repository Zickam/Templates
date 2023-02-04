from loguru import logger

path_to_append = os.getcwd()
if __name__ == "__main__":
    path_to_append = os.path.abspath(os.path.join(__file__, "../../"))
    sys.path.append(path_to_append)

import config

file_name = os.path.basename(__file__)
logs_file_path = os.path.abspath(os.path.join(path_to_append, config.LOGS_PATH, f"{file_name}.log"))
logger.add(logs_file_path, format="{time} {level} {message}",
level="DEBUG", rotation="1MB", compression="zip")