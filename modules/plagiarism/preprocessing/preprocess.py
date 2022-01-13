from modules.plagiarism.preprocessing import vectorizedocument
from modules.plagiarism.preprocessing import parasplitter
from modules.plagiarism.preprocessing import removepunctuations
from modules.plagiarism.preprocessing import removebullets
from modules.plagiarism.preprocessing import tokenizer
import spacy, en_core_web_lg
sp = en_core_web_lg.load()
import re
import string
from unidecode import unidecode

def preprocess(text):
    """ Preprocess a given text """
    
    s = vectorizedocument.text_to_list(text)
    t = []
    for i in s:
        t.append(parasplitter.sbd(i))
    t = removepunctuations.removesb(t)
    t = removebullets.removebullets(t)
    for i in t:
        s.append(tokenizer.removeWhiteSpace(i))
    return list(set(s))


def preprocessURL(text):
    """ Preprocess a given text from a URL """
    
    s = vectorizedocument.text_to_list(text)
    t = []
    for i in s:
        t.append(parasplitter.sbd(i))
    t = removepunctuations.removesb(t)
    t = removebullets.removebullets(t)
    for i in t:
        s.append(tokenizer.removeWhiteSpace(i))
    return s


def preprocess_train(text):
    """ Preprocess a given text """
    
    s = vectorizedocument.text_to_list_all(text)
    t = []
    for i in s:
        t.append(parasplitter.sbd(i))
    t = removepunctuations.removesb(t)
    t = removebullets.removebullets(t)
    s = []
    for i in t:
        s.append(tokenizer.removeWhiteSpace(i))
    return s
