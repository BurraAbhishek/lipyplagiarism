# Normalized Word Mover's Distance

from gensim import models

# If this code fails to run, you need to download the GloVe dataset.
# Open a file explorer, then go to modules/plagiarism/comparisons/datasets/
# Create a new folder "glove6b" and go to the following link to download the dataset:
# https://nlp.stanford.edu/data/wordvecs/glove.6B.zip
# Then use the 50d model. If any other model is used, change the file name accordingly.
# Before you can use the model, open a terminal or its equivalent in the same folder, then run
# python -m gensim.scripts.glove2word2vec --input  glove.6B.50d.txt --output glove.6B.50d.w2vformat.txt
w = models.KeyedVectors.load_word2vec_format(
    'modules/plagiarism/comparisons/datasets/glove6b/glove.6B.50d.w2vformat.txt', binary=False)

# w.init_sims may throw a deprecation warning, use fill_norms instead.
# w.init_sims(replace=True)
w.fill_norms()

def nwmd(dataframe):
    dataframe["Normalized Word Mover's Distance"] = dataframe.apply(
        lambda x: w.wmdistance(x[0], x[1]), 
        axis=1
        )
    return dataframe
