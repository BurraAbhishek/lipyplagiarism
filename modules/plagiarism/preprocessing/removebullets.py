def removebullets(text):
    """ Remove bullet points from each sentence. """

    t = []
    for p in text:
        if len(p) > 2:
            if p[0] == "*":
                t.append(p[2:])
            else:
                t.append(p)
        else:
            t.append(p)
    return t