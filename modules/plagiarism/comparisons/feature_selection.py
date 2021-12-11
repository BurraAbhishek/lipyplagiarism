import pandas as pd
from modules.plagiarism.comparisons.lexical import fuzzysimilarity, nlcs, ngram
from modules.plagiarism.comparisons.semantic import nwmd
from modules.plagiarism.comparisons.syntactic import generateoverlaps

def get_features(data_list):
    x = pd.DataFrame(data_list)
    x = (nlcs.apply_nlcs(fuzzysimilarity.fuzzysimilarity(x)))
    x = (ngram.ngram_features(x))
    x = (nwmd.nwmd(x))
    #x = (generateoverlaps.syntactics(x))
    return x