import csv

from org.yiming.analyzer.nlp_processor import NLPProcessor
from org.yiming.executor.abstract_file_executor import AbstractFileExecutor
from org.yiming.parser.page_parser_selector import PageParserSelector

HEADERS = ['WORD/PHRASE', 'OCCURRENCES']


class WordCountFileExecutor(AbstractFileExecutor):

    def __init__(self):
        self.nlp_processor = NLPProcessor()

    def pre_execute(self):
        pass

    def internal_execute(self, input_file_name, **kwargs):
        parser = PageParserSelector.get_parser(input_file_name)
        total_page_number = parser.total_page_number()
        print('The total page count of file ' + input_file_name + ' is ' + str(total_page_number))
        result = []
        for page_no in range(total_page_number):
            text = parser.extract_page_text(page_no)
            result.append(self.nlp_processor.process(text, **kwargs))

        return result

    def output_result(self, output_file, analyze_data):
        output_format = {}
        for paged_data in analyze_data:
            for item_data in paged_data.values():
                for stem_token, count in item_data.items():
                    if stem_token not in output_format:
                        output_format[stem_token] = 0
                    output_format[stem_token] += count

        print("start writing to output CSV file " + output_file)
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            for word, count in output_format.items():
                writer.writerow([word, count])
        print("successfully writing to output CSV file " + output_file)
