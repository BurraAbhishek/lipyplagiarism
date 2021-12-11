from sklearn.linear_model import LogisticRegression

def train_lr(Xtrain, Ytrain):
    lrModel = LogisticRegression(max_iter=10000)
    lrModel.fit(Xtrain, Ytrain)
    return lrModel
    