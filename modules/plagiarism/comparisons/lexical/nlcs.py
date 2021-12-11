def NLCS(sentence1, sentence2):
    """ Determine the length of the NLCS of two sentences """

    # Get each individual word from each of the sentences.
    word1 = sentence1.split()
    word2 = sentence2.split()

    # Get the number of words from each sentence.
    l1 = len(word1)
    l2 = len(word2)

    # Initialize the nested list to store all the 
    # subsequence similarity values
    a = []
    for i in range(l1 + 1):
        l = []
        for j in range(l2 + 1):
            l.append([])
        a.append(l)

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            # Nothing to compare initially
            if i == 0 or j == 0:
                a[i][j] = 0
            # Matching words
            # Add 1 to the subsequence
            elif word1[i - 1] == word2[j - 1]:
                a[i][j] = a[i - 1][j - 1] + 1
            # Words do not match
            # Get the maximum value of its previous neighbours
            else:
                a[i][j] = max(a[i-1][j], a[i][j-1])
    
    # a[l1][l2] contains the length of the 
    # longest common subsequence of X[0..n-1] & Y[0..m-1] 
    lf = a[l1][l2]/(len((set(word1).union(set(word2)))))
    
    # lf is the length of the Normalized longest common subsequence
    return lf


def apply_nlcs(dataframe):
    dataframe["Normalized Longest Common Subsequence"] = dataframe.apply(lambda x: NLCS(x[0], x[1]), axis=1)
    return dataframe