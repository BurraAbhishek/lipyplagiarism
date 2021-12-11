import pandas as pd
from modules.plagiarism.comparisons import feature_selection
from modules.plagiarism.comparisons import dspreprocessing
from modules.plagiarism.comparisons import X_Y_split


def dsSplitter(l):
    x = feature_selection.get_features(l)

    # At this stage we have our dataset
    x = dspreprocessing.preprocess_ds(x)

    # Scaling the dataset
    X, Y = X_Y_split.x_y_split(x)
    X = pd.DataFrame(dspreprocessing.scale_df(X))
    y = Y.values.tolist()
    Y = []
    for i in y:
        Y.append(i[0])
    return X, Y