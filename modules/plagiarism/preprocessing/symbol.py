from modules.plagiarism.preprocessing import replacer

def substitute_symbol(s):
    """ Substitute symbols with their literal counterparts. """
    
    replacer.replace(s, "$", "dollar")
    replacer.replace(s, "%", "percent")
    replacer.replace(s, "&", "and")
    return s

