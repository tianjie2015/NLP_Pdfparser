from nltk.tokenize import word_tokenize
from nltk.stem import *


class WordCountAnalyzer:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def __del__(self):
        del self.stemmer

    def count_a_word_in_text(self, word, text):
        if not text:
            return 0
        page_text = text.lower()
        page_tokens = word_tokenize(page_text)
        page_stems = [self.stemmer.stem(s.lower()) for s in page_tokens]
        w_stem = self.stemmer.stem(word.lower())
        count = page_stems.count(w_stem)
        return count

    def count_words_in_text(self, words, text):
        if not text:
            return {}
        result = {}
        page_text = text.lower()
        page_tokens = word_tokenize(page_text)
        page_stems = [self.stemmer.stem(s.lower()) for s in page_tokens]
        for word in words:
            w_stem = self.stemmer.stem(word.lower())
            count = page_stems.count(w_stem)
            result[word] = count
        return result

    def count_phrases_in_text(self, phrases, text):
        if not text:
            return {}
        text = text.replace('-', ' ')
        result = {}
        page_text = text.lower()
        page_tokens = word_tokenize(page_text)
        token_text = ' '.join(page_tokens)
        for p in phrases:
            flatten_p = ' '.join(p)
            count = token_text.count(flatten_p)
            dash_p = '-'.join(p)
            result[dash_p] = count
        return result
