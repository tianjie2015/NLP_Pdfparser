from PyPDF2 import PdfFileReader


class PdfParser:

    def __init__(self, file_name):
        self.f = open(file_name, 'rb')
        self.pdf = PdfFileReader(self.f, strict=False)

    def __del__(self):
        self.f.close()
        del self.f, self.pdf

    def page_number(self):
        return self.pdf.numPages

    def extract_page_text(self, page_number=0):
        page_text = self.pdf.getPage(page_number).extract_text()
        # print "page text " + page_text
        return page_text

