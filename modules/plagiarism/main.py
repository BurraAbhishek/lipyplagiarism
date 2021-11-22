from modules.plagiarism.preprocessing import vectorizedocument
from modules.plagiarism.preprocessing import parasplitter
from modules.plagiarism.preprocessing import removepunctuations
from modules.plagiarism.preprocessing import removebullets

def preprocess(text):
    """ Preprocess a given text """
    
    s = vectorizedocument.text_to_list(text)
    t = []
    for i in s:
        t.append(parasplitter.sbd(i))
    t = removepunctuations.removesb(t)
    #t = removebullets.removebullets(t)
    return t


def calculate_plagiarism(text):
    t = preprocess(text)
    return t
