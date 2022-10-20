from org.yiming.analyzer.abstract_analyzer import AbstractAnalyzer

from nltk.tokenize import word_tokenize


class WordsAnalyzer(AbstractAnalyzer):

    def __init__(self, stemmer):
        self.stemmer = stemmer

    def __del__(self):
        del self.stemmer

    def analyze(self, candidates, text):
        if not text:
            return {}
        result = {}
        page_text = text.lower()
        page_tokens = word_tokenize(page_text)
        page_stems = [self.stemmer.stem(s.lower()) for s in page_tokens]
        for word in candidates:
            w_stem = self.stemmer.stem(word.lower())
            count = page_stems.count(w_stem)
            result[word] = count
        return result
