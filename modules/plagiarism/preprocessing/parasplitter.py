import nltk

def sbd(text):
    """
    Sentence Boundary Disambiguation for paragraphs
    Split a paragraph into sentences.
    """

    sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer()
    sentences = sent_tokenizer.tokenize(text)
    return sentences