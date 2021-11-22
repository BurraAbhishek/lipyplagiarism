import re

def ignore_topics_list():
    """ 
    A list of headings or topics to be ignored by the plagiarism checker 
    """

    return [
        'references',
        'citations',
        'references and citations',
        'citations and references'
        ]


def ignore_topics(sentences):
    """ 
    Exclude the ignored portions of the text from the checker

    Parameters: list of sentences

    Returns: list of sentences
    """

    l = ignore_topics_list()
    n = len(sentences)
    for i in range(0, n):
        if sentences[i] in l:
            for j in range(n - 1, i - 1, -1):
                sentences.pop()
            break
    n = len(sentences)
    if re.match("\S", sentences[n - 1]) or (len(sentences[n - 1]) == 0):
        sentences.pop()
    return sentences