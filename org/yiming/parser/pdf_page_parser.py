from org.yiming.parser.abstract_page_parser import AbstractPageParser

from PyPDF2 import PdfFileReader


class PdfPageParser(AbstractPageParser):

    def __init__(self, file_name):
        self.file_name = file_name
        self.f = open(file_name, 'rb')
        self.pdf = PdfFileReader(self.f, strict=False)

    def __del__(self):
        self.f.close()
        del self.f, self.pdf

    def total_page_number(self):
        return self.pdf.numPages

    def extract_page_text(self, page_number):
        page_text = self.pdf.getPage(page_number).extract_text()
        return page_text
