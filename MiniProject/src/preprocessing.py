import pandas as pd

def preprocess_data(df):

    # convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # extract month
    df["Month"] = df["Date"].dt.month

    print("\nPreprocessing Completed")

    return df