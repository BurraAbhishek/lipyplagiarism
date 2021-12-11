from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def fuzzysimilarity(dataframe):
    """
    Compares two strings in a Pandas DataFrame: dataframe[0], dataframe[1]
    String comparison using Levenshtein distance
    to calculate distance between sequences.
    We need all ratios
    """

    # Fuzz ratio: similarity of entire string
    dataframe['Fuzz Ratio'] = dataframe.apply(lambda x: fuzz.ratio(str(x[0]), str(x[1])), axis=1)

    # Fuzz Token Set Ratio: similarity of each token in the string
    # The word order does not matter, unlike in fuzz ratio
    dataframe['Fuzz Token Set Ratio'] = dataframe.apply(
        lambda x: fuzz.token_set_ratio(str(x[0]), str(x[1])), 
        axis=1
        )

    return dataframe