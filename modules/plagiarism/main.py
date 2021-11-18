from modules.plagiarism.preprocessing import vectorizedocument
from modules.plagiarism.preprocessing import parasplitter

def preprocess(text):
    s = vectorizedocument.text_to_list(text)
    t = []
    for i in s:
        t.append(parasplitter.sbd(i))
    for i in t:
        print(i)
    return t


def calculate_plagiarism(text):
    return preprocess(text)
