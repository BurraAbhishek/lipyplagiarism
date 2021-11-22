import string

def removesb(text):
    """ Remove all punctuation marks from each sentence. """

    t = []
    for j in text:
        for i in j:
            p = "".join(word for word in i if word not in string.punctuation)
            t.append(p)
    return t