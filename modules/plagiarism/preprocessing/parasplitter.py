import nltk

def sbd(text):
    sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer()
    sentences = sent_tokenizer.tokenize(text)
    return sentences