from org.yiming.analyzer.abstract_analyzer import AbstractAnalyzer

from nltk.tokenize import word_tokenize


class PhrasesAnalyzer(AbstractAnalyzer):
    def __init__(self, stemmer):
        self.stemmer = stemmer

    def __del__(self):
        del self.stemmer

    def analyze(self, candidates, text):
        if not text:
            return {}
        text = text.replace('-', ' ')
        result = {}
        page_text = text.lower()
        page_tokens = word_tokenize(page_text)
        token_text = ' '.join(page_tokens)
        for p in candidates:
            flatten_p = ' '.join(p)
            count = token_text.count(flatten_p)
            dash_p = '-'.join(p)
            result[dash_p] = count
        return result
