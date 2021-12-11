import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_ds(df):
    df.drop(1, inplace=True, axis=1)
    df.drop(0, inplace=True, axis=1)
    return df


def scale_df(df):
    scaler = StandardScaler()
    v = df.values.tolist()
    df_scaled = pd.DataFrame(scaler.fit_transform(v))
    return df_scaled
