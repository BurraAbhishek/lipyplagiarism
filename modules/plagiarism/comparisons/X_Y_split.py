import pandas as pd

def x_y_split(df):
    Y = pd.DataFrame(df[2])
    df.drop(2, inplace=True, axis=1)
    return df, Y