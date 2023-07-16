import pathlib

from app.config import FILES_INPUT_DIR
from app.loggers.loggers import get_custom_logger


def check_file_exists():
    file_path = FILES_INPUT_DIR.joinpath("test.txt")
    if file_path.exists():
        print(f"File exists: {file_path.as_uri()}")
    else:
        raise FileNotFoundError(f"File not found: {file_path.as_uri()}")


def read_file(file_path: pathlib.Path = None):
    logger = get_custom_logger(__name__)
    logger.info(f"start read file: {file_path}")
    if file_path is None:
        file_path = FILES_INPUT_DIR.joinpath("test.txt")
    with open(file_path) as file:
        for line in file:
            print(line, end="")
    print("")
