import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def evaluate_clustering(X, labels):
    """
    Evaluate the clustering results using silhouette score.
    Args:
        X (array-like): The feature data used for clustering.
        labels (array-like): The cluster labels assigned to each data point.
    Returns:
        float: The silhouette score indicating the quality of the clustering.
    """
    score = silhouette_score(X, labels)
    print(f"\nSilhouette Score: {score}")

    #save result
    eval_df = pd.DataFrame({
        "metric": ["silhouette_score"],
        "value": [score]
    })
    eval_df.to_csv("data/models/clustering_evaluation.csv", index=False)
    return score

def run_model():
    """
    Run the clustering model for cereal data. This function loads the processed cereal nutrient dataset, 
    selects key nutritional features, and applies KMeans clustering to identify groups of similar cereals. 
    The resulting clusters are then summarized and saved for further analysis.

        returns:
            None (saves outputs to CSV files)

    """

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

    # Preprocessing

    X = X.fillna(0)


    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Model

    kmeans = KMeans(
        n_clusters=4,
        random_state=42
    )


    df["cluster"] = kmeans.fit_predict(X_scaled)

    # Add cluster names

    cluster_names = {
        0: "Whole Grain / High Fiber",
        1: "High Protein / Health",
        2: "Sugary Cereals",
        3: "High Sodium / Processed"
    }


    df["cluster_name"] = df["cluster"].map(cluster_names)
    


    # Evaluation

    score = evaluate_clustering(X_scaled, kmeans.labels_)
    cluster_summary = df.groupby("cluster_name")[features].mean()
   

    print("\nCluster Summary:\n")
    print(cluster_summary)
    print(score)

    # Save outputs
  
    df.to_csv(
        "data/models/clustering_results.csv",
        index=False
    )


    cluster_summary.to_csv(
        "data/models/clustering_summary.csv"
    )

    



if __name__ == "__main__":
    run_model()