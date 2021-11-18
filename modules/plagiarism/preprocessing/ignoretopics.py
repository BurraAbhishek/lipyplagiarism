import re

def ignore_topics_list():
    return [
        'references',
        'citations',
        'references and citations',
        'citations and references'
        ]


def ignore_topics(sentences):
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