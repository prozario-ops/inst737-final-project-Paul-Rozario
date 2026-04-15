from pyexpat import model

import pandas as pd
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import logging

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
    evaluate_trend(y, df["predicted"])

    # Evaluation

    slope = model.coef_[0]

    print("\nTrend slope:", slope)

    # Save output
    
    df.to_csv(
        "data/models/fmap_trend_results.csv",
        index=False
    )
    if df is not None:
        logging.info("model_2.py run_model() successful")
    else:
        logging.error("model_2.py run_model() failed")

def evaluate_trend(y_true, y_pred):
    """
    Evaluate the purchase trend model using R2 and RMSE metrics.
    Args:
        y_true (array): The true values of the target variable.
        y_pred (array): The predicted values from the model.
        Returns:
            None (prints evaluation metrics and saves them to a CSV file)
    """
    # Calculate evaluation metrics
    r2 = r2_score(y_true, y_pred)
    rmse =np.sqrt(mean_squared_error(y_true, y_pred))
    # print evaluation results
    print(f"\nR2: {r2}")
    if r2 > 0.7:
        print("(Good fit, this indicates a strong trend in purchase dollars over time)")
    elif r2 > 0.4:
        print("(Moderate fit, this indicates a moderate trend in purchase dollars over time)")
    else:
        print("(Poor fit, this indicates a weak or no trend in purchase dollars over time)")
    print(f"RMSE: {rmse}")
    if rmse < 1000:
        print("(Good fit, this indicates that the model's predictions are close to the actual values)")
    elif rmse < 5000:
        print("(Moderate fit, this indicates that the model's predictions are moderately close to the actual values)")
    else:
        print("(Poor fit, this indicates that the model's predictions are not close to the actual values). ")
    # Save evaluation results to CSV
    eval_df= pd.DataFrame({
        "metric":["r2", "rmse"],
        "value": [r2, rmse]
    })
    

    eval_df.to_csv("data/models/model_evaluation/trend_evaluation.csv", index=False)
    if eval_df is not None:
        logging.info("model_2.py evaluate_trend() successful")
    else:
        logging.error("model_2.py evaluate_trend() failed")

if __name__ == "__main__":
    run_model()
    evaluate_trend()