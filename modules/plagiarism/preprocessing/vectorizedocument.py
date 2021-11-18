from modules.plagiarism.preprocessing import symbol, ignoretopics 

def text_to_list(text):
    s = symbol.substitute_symbol(text)
    s = s.lower()
    a = s.split("\r\n")
    b = ignoretopics.ignore_topics(a)
    return b
