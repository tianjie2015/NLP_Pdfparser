from pathlib import Path

from org.yiming.configuration.configuration import FOLDER, OUT_FOLDER, PHRASES, WORDS, FILE_NAMES
from org.yiming.executor.world_count_file_executor import WordCountFileExecutor

from nltk import download


def execute_one_file(file_name):
    download('punkt')
    executor = WordCountFileExecutor()
    input_file = FOLDER + file_name
    output_file = OUT_FOLDER + file_name.replace('.pdf', '.csv')
    Path(OUT_FOLDER).mkdir(parents=True, exist_ok=True)
    executor.execute(input_file, output_file, words=WORDS, phrases=PHRASES)


def execute_files():
    for file_name in FILE_NAMES:
        execute_one_file(file_name)


if __name__ == '__main__':
    execute_files()
