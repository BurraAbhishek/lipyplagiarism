def removeR(s):
    return s.replace("\r", "")


def removeN(s):
    return s.replace("\n", " ")


def removeLines(s):
    """ Replace \\r and \\n with a space. """

    return removeR(removeN(s))
