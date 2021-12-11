from nltk.util import ngrams

def jaccardDistance(x, y, n):
    _w1, _w2, a, b = common_ngrams(x, y, n)
    l = len(set(a).union(set(b)))
    if l == 0:
        return 0
    else:
        return len(set(a).intersection(set(b))) / l


def ngrams_ratio(a, b, n):
    w1, w2, ngrams1, ngrams2 = common_ngrams(a, b, n)
    return len(set(ngrams1).intersection(set(ngrams2))) / (len(w1) + len(w2))


def common_ngrams(a, b, n):
    # Split the sentences into words
    w1 = a.split()
    w2 = b.split()
    # Get the n grams
    ngrams1 = list(ngrams(w1, n))
    ngrams2 = list(ngrams(w2, n))
    return w1, w2, ngrams1, ngrams2


def ngram_features(df):
    df['Common Unigram Ratio'] = df.apply(
        lambda x: ngrams_ratio(str(x[0]), str(x[1]), 1), 
        axis=1
        )
    df['Common Bigram Ratio'] = df.apply(
        lambda x: ngrams_ratio(str(x[0]), str(x[1]), 2), 
        axis=1
        )
    df['Common Trigram Ratio'] = df.apply(
        lambda x: ngrams_ratio(str(x[0]), str(x[1]), 3), 
        axis=1
        )
    df['Unigram Jaccard Distance'] = df.apply(
        lambda x: jaccardDistance(str(x[0]), str(x[1]), 1), 
        axis=1
        )
    df['Bigram Jaccard Distance'] = df.apply(
        lambda x: jaccardDistance(str(x[0]), str(x[1]), 2), 
        axis=1
        )
    df['Trigram Jaccard Distance'] = df.apply(
        lambda x: jaccardDistance(str(x[0]), str(x[1]), 3), 
        axis=1
        )
    return df
