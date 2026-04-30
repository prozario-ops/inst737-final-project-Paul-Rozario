import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import logging

def run_model():
    """
    Run the clustering model for cereal data. This function loads the processed cereal nutrient dataset, 
    selects key nutritional features, and applies KMeans clustering to identify groups of similar cereals. 
    The resulting clusters are then summarized and saved for further analysis.

        returns:
            None (saves outputs to CSV files)

    """

    # load processed dataset
    logging.info("model_1.py run_model() started")

    df = pd.read_csv("data/processed/cereal_nutrients.csv")

    # dsired nutrition features

    features = [
        "Protein",
        "Total lipid (fat)",
        "Carbohydrate",
        "Total Sugars",
        "Fiber",
        # "Sodium"
        
    ]

    X = df[features].copy()

    # Preprocessing

    X = X.fillna(0)
    for col in features:
        upper = X[col].quantile(0.95)
        X[col] = X[col].clip(upper=upper)


    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Model

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )


    df["cluster"] = kmeans.fit_predict(X_scaled)

    centers = pd.DataFrame(
        scaler.inverse_transform(kmeans.cluster_centers_),
        columns=features
    )

    logging.info("Cluster Centers")
    logging.info("\n" + centers.to_string())

    
    # improved cluster naming logic based on nutrient profiles
    
    cluster_names = {}

    for i, row in centers.iterrows():
        if row["Total Sugars"] > 25:
            cluster_names[i] = "Sugary Cereals"
        elif row["Protein"] > 10:
            cluster_names[i] = "High Protein / Health"
        elif row["Fiber"] > 8:
            cluster_names[i] = "Whole Grain / High Fiber"
        # elif row["Sodium"] > 500:
        #     cluster_names[i] = "High Sodium / Processed"
        else:
            cluster_names[i] = "Balanced Cereals"

    df["cluster_name"] = df["cluster"].map(cluster_names)
    


    #evaluation

    cluster_summary = df.groupby("cluster_name")[features].mean()
    


    logging.info("Cluster Summary:")
    logging.info("\n" + cluster_summary.to_string())
    score = evaluate_clustering(X_scaled, kmeans.labels_)
   # print(score)
    if score>.2:
        logging.info("silhouette score is acceptable")
    else:        
        logging.error("consider revising clustering approach, silhouette score is low")

    # save outputs
  
    df.to_csv(
        "data/models/clustering_results.csv",
        index=False
    )


    cluster_summary.to_csv(
        "data/models/clustering_summary.csv"
    )

def evaluate_clustering(X, labels):
    """
    Evaluate the clustering results using silhouette score.
    Args:
        X (array-like): The feature data used for clustering.
        labels (array-like): The cluster labels assigned to each data point.
    Returns:
        float: The silhouette score indicating the quality of the clustering.
    """
    #calculate silhouette score
    score = silhouette_score(X, labels)
    logging.info(f"\nSilhouette Score: {score}")
    if score > 0.5:
        logging.info("Clustering is good (score > 0.5). This shows that cereals are well clustered based on their nutritional profiles.")
    elif score > 0.25:
        logging.info("Clustering is moderate (score between 0.25 and 0.5). This shows that cereals are somewhat clustered based on their nutritional profiles.")
    else:
        logging.info("Clustering is poor (score <= 0.25). This shows that cereals are not well clustered based on their nutritional profiles. ")

    #save result
    eval_df = pd.DataFrame({
        "metric": ["silhouette_score"],
        "value": [score]
    })
    eval_df.to_csv("data/models/model_evaluation/clustering_evaluation.csv", index=False)
    if eval_df is not None:
        logging.info("model_1.py evaluate_clustering successful")
    else:
        logging.error("model_1.py evaluate_clustering failed")
    return score
    



if __name__ == "__main__":
    run_model()