import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def run_model():

    # load processed dataset
    
    df = pd.read_csv("data/processed/cereal_nutrients.csv")

    # dsired nutrition features

    features = [
        "Protein",
        "Total lipid (fat)",
        "Carbohydrate",
        "Total Sugars",
        "Fiber",
        "Sodium"
    ]

    X = df[features]




if __name__ == "__main__":
    run_model()