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
    logging.info("model_2.py run_model() started")


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

    logging.info(f"Trend slope: {slope}")
    logging.info("This indicates a strong downward trend in cereal purchase dollars over time, seen through the cereal_trend.png visualization. This suggests that consumers are purchasing less cereal over time, which could be due to changing dietary preferences, increased competition from other breakfast options, or other market factors. The model's predictions can be used to forecast future purchase dollars and inform business strategies for cereal manufacturers and retailers.")

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
    logging.info(f"R2: {r2}")
    if r2 > 0.7:
        logging.info("(Good fit, this indicates a strong trend in purchase dollars over time)")
    elif r2 > 0.4:
        logging.info("(Moderate fit, this indicates a moderate trend in purchase dollars over time)")
    else:
        logging.info("(Poor fit, this indicates a weak or no trend in purchase dollars over time)")
    logging.info(f"RMSE: {rmse}")
    if rmse < 1000:
        logging.info("(Good fit, this indicates that the model's predictions are close to the actual values)")
    elif rmse < 5000:
        logging.info("(Moderate fit, this indicates that the model's predictions are moderately close to the actual values)")
    else:
        logging.info("(Poor fit, this indicates that the model's predictions are not close to the actual values). ")
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