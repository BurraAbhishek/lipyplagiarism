def removeR(s):
    return s.replace("\r", "")


def removeN(s):
    return s.replace("\n", " ")

def removeLines(s):
    return removeR(removeN(s))
