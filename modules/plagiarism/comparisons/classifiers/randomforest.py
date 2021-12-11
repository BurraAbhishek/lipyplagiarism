from sklearn.ensemble import RandomForestClassifier

def rfModel(Xtrain, Ytrain):
    rf = RandomForestClassifier()
    rf.fit(Xtrain, Ytrain)
    return rf