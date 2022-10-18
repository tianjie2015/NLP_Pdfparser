import csv
import itertools

from multiprocessing import Pool
from pathlib import Path

from org.yiming.analyzer.word_count_analyzer import WordCountAnalyzer
from org.yiming.configuration.configuration import FILE_NAMES, FOLDER, OUT_FOLDER, PHRASES, WORDS
from org.yiming.executor.pre_executor import pre_execute
from org.yiming.parser.pdf_parser import PdfParser

NUMBER_OF_PROCESSOR_IN_POOL = 10

HEADERS = ['WORD/PHRASE', 'OCCURRENCES']

raw_parsers = {f_n: PdfParser(FOLDER + f_n) for f_n in FILE_NAMES}
raw_analyzer = WordCountAnalyzer()


def task(pager_number, words, phrases, file_name):
    raw_parser = raw_parsers.get(file_name)
    text = raw_parser.extract_page_text(pager_number)
    words_count = raw_analyzer.count_words_in_text(words, text)
    phrases_count = raw_analyzer.count_phrases_in_text(phrases, text)
    return [words_count, phrases_count]


def task_star(p_w_p_f):
    return task(*p_w_p_f)


def words_count_in_file(file_name, words, phrases):
    raw_parser = raw_parsers.get(file_name)
    total_page_number = raw_parser.page_number()
    pool = Pool(NUMBER_OF_PROCESSOR_IN_POOL)
    args = zip(range(total_page_number), itertools.repeat(words), itertools.repeat(phrases), itertools.repeat(file_name))
    task_result = pool.map(task_star, args)
    pool.close()
    pool.join()
    flatten_word_counts = {}
    for item in task_result:
        w_counts, p_counts = item
        w_counts.update(p_counts)
        for word, count in w_counts.items():
            if word not in flatten_word_counts:
                flatten_word_counts[word] = 0
            flatten_word_counts[word] += w_counts.get(word, 0)
    return flatten_word_counts


def execute_one_file(file_name):
    print("start parsing file " + file_name + " and count words " + str(WORDS) + " and phrases " + str(PHRASES))
    word_counts = words_count_in_file(file_name, WORDS, PHRASES)
    print("Successfully parsing file " + file_name + " and count words " + str(WORDS) + " and phrases " + str(PHRASES))

    output_file = file_name.replace('.pdf', '.csv')
    Path(OUT_FOLDER).mkdir(parents=True, exist_ok=True)
    print("start writing to output CSV file " + output_file)
    with open(OUT_FOLDER + output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        for word, count in word_counts.items():
            writer.writerow([word, count])
    print("successfully writing to output CSV file " + output_file)


def execute_files():
    for file_name in FILE_NAMES:
        execute_one_file(file_name)


if __name__ == '__main__':
    pre_execute()
    execute_files()
