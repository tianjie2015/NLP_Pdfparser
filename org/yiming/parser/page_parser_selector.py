from org.yiming.parser.pdf_page_parser import PdfPageParser


class PageParserSelector(object):

    @staticmethod
    def get_parser(file_name):
        if file_name.lower().endswith('.pdf'):
            return PdfPageParser(file_name)
        raise KeyError('Can not find Parser for File ' + file_name + '. File type is not supported .')
