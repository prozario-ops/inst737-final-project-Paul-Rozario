import pandas as pd
from sklearn.linear_model import LinearRegression


def run_model():
    """
    
    Run the purchase trend model. This function loads the processed FMAP price timeseries dataset,
    preprocesses the data, and applies a linear regression model to identify trends in purchase dollars over time.
    The resulting trend slope is printed, and the predictions are saved for further analysis.

        returns:
            None (saves outputs to CSV files)
    """
    #load transformed data


    df = pd.read_csv("data/processed/cereal_price_timeseries.csv")

    # pre-processing

    df["date"] = pd.to_datetime(df["date"])
    df["time_index"] = range(len(df))

    # Model

    X = df[["time_index"]]
    y = df["Purchase_dollars_wtd"]

    model = LinearRegression()
    model.fit(X, y)

    df["predicted"] = model.predict(X)

    # Evaluation

    slope = model.coef_[0]


    print("\nTrend slope:", slope)

    # Save output

    df.to_csv(
        "data/models/fmap_trend_results.csv",
        index=False
    )


if __name__ == "__main__":
    run_model()