from modules.plagiarism.preprocessing import replacer

def substitute_symbol(s):
    replacer.replace(s, "$", "dollar")
    replacer.replace(s, "%", "percent")
    replacer.replace(s, "&", "and")
    return s

