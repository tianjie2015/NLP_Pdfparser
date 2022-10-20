from org.yiming.analyzer.phrases_analyzer import PhrasesAnalyzer
from org.yiming.analyzer.words_analyzer import WordsAnalyzer

from nltk.stem import PorterStemmer


class NLPProcessor(object):
    WORD_KEY = 'words'
    PHRASE_KEY = 'phrases'

    def __init__(self):
        self.stemmer = PorterStemmer()
        self.analyzers = {
            self.WORD_KEY: WordsAnalyzer(self.stemmer),
            self.PHRASE_KEY: PhrasesAnalyzer(self.stemmer)
        }

    def process(self, text, **kwargs):
        result = {}
        for input_type, candidates in kwargs.items():
            analyzer = self.analyzers[input_type]
            result[input_type] = analyzer.analyze(candidates, text)
        return result
