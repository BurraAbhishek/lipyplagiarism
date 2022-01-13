import pandas as pd
from modules.plagiarism.preprocessing import preprocess
from modules.plagiarism.comparisons import ds_splitter
from modules.plagiarism.comparisons.classifiers import logistic, randomforest
from sklearn import metrics


def get_train_df(location):
    train_file = open(location, mode='r')
    unprocessed_train_data = list([example.split("\t") for example in train_file.readlines()])[1:]
    for i in unprocessed_train_data:
        i.pop(0)
        i[2] = int(i[2].replace("\n", ""))
    return unprocessed_train_data


def process_dataset(dataset):
    for i in dataset:
        i[0] = preprocess.preprocess_train(i[0])[0]
        i[1] = preprocess.preprocess_train(i[1])[0]
    return dataset


def get_model_dataset(modelfile):
    print("Fetching training models...")
    y = process_dataset(get_train_df(modelfile))
    print("Generating datasets (1 of 2)...")
    X, Y = ds_splitter.dsSplitter(y)
    print("Generating datasets (2 of 2)...")
    return X, Y

X, Y = get_model_dataset(modelfile='modules/plagiarism/comparisons/datasets/final/train.tsv')

lrModel = logistic.train_lr(X, Y)
print("Training models (1 of 2)...")
rfModel = randomforest.rfModel(X, Y)
print("Training models (2 of 2)...")

y1 = process_dataset(get_train_df('modules/plagiarism/comparisons/datasets/final/test.tsv'))
s1 = "I am a boy"
s2 = "I am a girl"

#y1 = [[s1, s1, 1], [s1, s2, 1], [s2, s2, 1], ["Mr. Thuso Nokwanda Mbedu was born in Pietermaritzburg as Thuso Mbebu", "Thuso Nokwanda Mbedu was born Thuso Mbebu in Pietermaritzburg", 1]]
X1, Y1 = ds_splitter.dsSplitter(y1)

Y2 = lrModel.predict(pd.DataFrame(X1))

Y3 = rfModel.predict(pd.DataFrame(X1))

X2 = X1.values.tolist()
for i in range(0, len(y1)):
    # Obvious lazy plagiarism is sometimes missed.
    if y1[i][0] == y1[i][1]:
        Y2[i] = 1
        Y3[i] = 1

print("Logistic Regression Accuracy: ", metrics.accuracy_score(Y1, Y2))
print("Random Forest Accuracy: ", metrics.accuracy_score(Y1, Y3))
print("Logistic Regression Precision: ", metrics.precision_score(Y1, Y2))
print("Random Forest Precision: ", metrics.precision_score(Y1, Y3))
