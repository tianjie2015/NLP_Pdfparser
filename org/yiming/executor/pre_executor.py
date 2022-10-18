import nltk


def nltk_install_repos():
    nltk.download('punkt')


def pre_execute():
    nltk_install_repos()
