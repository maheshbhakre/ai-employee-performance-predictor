import joblib
import pandas as pd

def load_model(model_path):
    return joblib.load(model_path)

def predict(model, input_df):
    return model.predict(input_df)

def predict_proba(model, input_df):
    return model.predict_proba(input_df)