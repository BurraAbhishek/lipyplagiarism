from unidecode import unidecode

def deaccent(text):
    """ Convert accented characters into literal counterpart. """

    t = []
    for tokens in text:
        tokens = [unidecode(token) for token in tokens]
        p = "".join([token for token in tokens])
        t.append(p)
    return t
  