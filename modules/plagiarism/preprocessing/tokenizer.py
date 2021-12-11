from nltk.tokenize import word_tokenize

def tokenize(sentence):
    """ Convert a sentence into words. """

    return word_tokenize(sentence)


def removeWhiteSpace(sentence):
    "Remove all whitespaces except for the word splitting whitespaces"

    tokens = sentence.split(" ")
    tokens_new = [t for t in tokens if len(t) > 0]
    processed = " ".join([t for t in tokens_new])
    return processed