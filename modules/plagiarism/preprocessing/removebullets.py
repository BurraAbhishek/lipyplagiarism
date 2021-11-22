def removebullets(text):
    """ Remove bullet points from each sentence. """

    t = []
    for p in text:
        if p[0] == "*":
            t.append(p[2:])
    return t