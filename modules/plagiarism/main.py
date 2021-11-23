from modules.plagiarism.preprocessing import preprocess


def calculate_plagiarism(text):
    t = preprocess.preprocess(text)
    return t
