from abc import abstractmethod, ABCMeta


class AbstractAnalyzer(metaclass=ABCMeta):

    @abstractmethod
    def analyze(self, candidates, text):
        "Analyze candidates in text based on NLP tokenizer"
        pass
