import pandas as pd
from sklearn.linear_model import LinearRegression


def run_model():
    #load transformed data


    df = pd.read_csv("data/processed/cereal_price_timeseries.csv")

    # pre-processing

    df["date"] = pd.to_datetime(df["date"])

    df["time_index"] = range(len(df))

if __name__ == "__main__":
    run_model()