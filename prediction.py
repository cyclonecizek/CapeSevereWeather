import joblib
import pandas as pd



def predict_15Z_offshore(data):
    clf_15Z_offshore = joblib.load("RFC_model_15Z_offshore.sav")
    prediction_15Z_offshore = clf_15Z_offshore.predict_proba(data)
    df_prob_15Z_offshore = pd.DataFrame(prediction_15Z_offshore)
    return df_prob_15Z_offshore[1]*100

def predict_10Z_updated(data):
    clf_10Z = joblib.load("RFC_model_limited_depth_10Z_updated.sav")
    prediction_10Z = clf_10Z.predict_proba(data)
    df_prob_10Z = pd.DataFrame(prediction_10Z)
    return df_prob_10Z[1]*100
