from modules.plagiarism.preprocessing import symbol, ignoretopics
from modules.plagiarism.preprocessing import accenter

def text_to_list(text):
    """ Convert the text into a list of preformatted sentences. """

    s = symbol.substitute_symbol(text)
    # Convert all characters to lowercase
    s = s.lower()
    # Convert text into list of paragraphs
    a = s.split("\r\n")
    b = ignoretopics.ignore_topics(a)
    b = accenter.deaccent(b)
    return b
