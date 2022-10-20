from abc import abstractmethod, ABCMeta


class AbstractPageParser(metaclass=ABCMeta):

    @abstractmethod
    def total_page_number(self):
        "get total page number of text"
        pass

    @abstractmethod
    def extract_page_text(self, page_number):
        "Get raw text of page based on page number"
        pass
