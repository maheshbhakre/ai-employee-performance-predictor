import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def split_features_target(df):
    X = df.drop("performance_rating", axis=1)
    y = df["performance_rating"]
    return X, y