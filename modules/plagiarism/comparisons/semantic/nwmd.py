# Normalized Word Mover's Distance

from gensim import models

w = models.KeyedVectors.load_word2vec_format(
    'modules/plagiarism/comparisons/datasets/glove6b/glove.6B.50d.w2vformat.txt', binary=False)

w.init_sims(replace=True)

def nwmd(dataframe):
    dataframe["Normalized Word Mover's Distance"] = dataframe.apply(
        lambda x: w.wmdistance(x[0], x[1]), 
        axis=1
        )
    return dataframe