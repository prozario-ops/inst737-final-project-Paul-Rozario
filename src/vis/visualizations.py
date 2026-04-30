import logging

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_clusters():
    """
    Visualize the cereal clusters using scatterplots and heatmaps. This function loads the clustering results,
    creates visualizations to illustrate the nutritional profiles of the identified clusters, and saves the plots for 
    further analysis.
        returns:
            None (saves outputs to PNG files)
    """
    logging.info("visualize_clusters() started")

    df = pd.read_csv("data/models/clustering_results.csv")

    # Remove unrealistic outliers

    df = df[
        (df["Total Sugars"] <= 60) &
        (df["Protein"] <= 40)
    ]

    # Scatterplot: Protein vs Sugar

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=df,
        x="Protein",
        y="Total Sugars",
        hue="cluster_name",
        alpha=0.6
    )

    plt.title("Cereal Nutrition Clusters")
    plt.xlabel("Protein (g)")
    plt.ylabel("Sugar (g)")
    plt.legend(title="Cluster Type")
    plt.tight_layout()
    plt.savefig("data/outputs/cereal_cluster_scatter.png")
    plt.show()
    logging.info("Scatter plot shows moderate separation between clusters, with sugary cereals grouping separately from higher protein and fiber cereals.")    
    logging.info("visualize_clusters() completed successfully") 
def visualize_cluster_profiles():
    """
    Create bar charts to visualize the average nutrient profiles of the cereal clusters. This function loads the clustering results,
    calculates the average values of key nutrients for each cluster, and generates bar charts to illustrate
    the differences in nutritional profiles across clusters. The bar charts are saved for further analysis.
        returns:
            None (saves outputs to PNG files)  
    """
    logging.info("visualize_cluster_profiles() started")

    # Load cluster summary
    df =pd.read_csv("data/models/clustering_summary.csv")


    df =df.reset_index()


    # Bar chart of protein per cluster
    plt.figure(figsize=(8,6))


    sns.barplot(
        data=df,
        x="cluster_name" ,
    y="Protein"
    )
    plt.title("Average Protein by Cereal Cluster")
    plt.xticks(rotation=15)
    plt.savefig("data/outputs/protein_cluster_bar.png")
    plt.show()
    logging.info("Protein comparison highlights clear differentiation, with high-protein cereals forming a distinct group.")
    logging.info("visualize_cluster_profiles() completed successfully")



def visualize_trend():
    """
    Visualize the purchasing trend over time using a line plot. This function loads the FMAP trend results,
    aggregates the purchase dollars by month, and creates a line plot to illustrate the trend in cereal
    purchasing over time. The plot is saved for further analysis.
        returns:
            None (saves outputs to PNG files)
    """
    logging.info("visualize_trend() started")
    df = pd.read_csv("data/models/fmap_trend_results.csv")
    df["date"] = pd.to_datetime(df["date"])


    # Aggregate monthly spending
    df = df.groupby("date")[["Purchase_dollars_wtd", "predicted"]].mean().reset_index()


    plt.figure(figsize=(10,6))
    plt.plot(df["date"], df["Purchase_dollars_wtd"], label="Actual Spending")
    plt.plot(df["date"], df["predicted"], label="Trend", linewidth=3)
    plt.title("Cereal Purchasing Trend Over Time")
    plt.xlabel("Year")
    plt.ylabel("Purchase Dollars")
    plt.legend()
    plt.tight_layout()
    plt.savefig("data/outputs/cereal_trend.png")
    plt.show()
    logging.info("Trend analysis indicates a slight decline in cereal purchasing over time, with high variability across periods.")
    logging.info("visualize_trend() completed successfully")


def visualize_cluster_heatmap():
    """
    Creates a heatmap to visualize the average nutrient profiles of the cereal clusters. This function loads the clustering results,
    calculates the average values of key nutrients for each cluster, and generates a heatmap to illustrate
    the differences in nutritional profiles across clusters. The heatmap is saved for further analysis.
   
        returns:
            None (saves outputs to PNG files)

    """
    logging.info("visualize_cluster_heatmap() started")
    df = pd.read_csv("data/models/clustering_results.csv")

    # Remove unrealistic values again
    df = df.copy()


    # Select nutrients for heatmap
   
    nutrients = [
        "Protein",
        "Total lipid (fat)",
        "Carbohydrate",
        "Total Sugars",
        "Fiber",
        "serving_size_grams",
       # "Sodium"
    ]

    cluster_summary = df.groupby("cluster_name")[nutrients].mean()
    # Heatmap


    plt.figure(figsize=(10,6))


    sns.heatmap(
        cluster_summary,
        annot=True,
        cmap="coolwarm",
        fmt=".1f"
    )

    plt.title("Average Nutrient Profile by Cereal Cluster")

    plt.ylabel("Cluster Type")
    plt.xlabel("Nutrients")
    plt.tight_layout()
    plt.savefig("data/outputs/cereal_cluster_heatmap.png")
    plt.show()
    logging.info("Cluster heatmap shows clear nutritional differences, with high protein, high sugar, and balanced fiber groups emerging across cereals.")
    logging.info("visualize_cluster_heatmap() completed successfully")
def visualize_cluster_counts():
    """
    Visualize the number of cereals in each cluster.
    args:        None
    returns:        None (saves output to PNG file)
    """
    logging.info("visualize_cluster_counts() started")
    df = pd.read_csv("data/models/clustering_results.csv")

    counts = df["cluster_name"].value_counts().reset_index()
    counts.columns = ["cluster_name", "count"]

    plt.figure(figsize=(8,6))

    sns.barplot(
        data=counts,
        x="cluster_name",
        y="count"
    )

    plt.title("Number of Cereals per Cluster")
    plt.xlabel("Cluster Type")
    plt.ylabel("Count")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("data/outputs/cluster_counts.png")
    plt.show()
    logging.info("Cluster distribution shows sugary cereals are most common, followed by fiber-focused and high-protein cereals.")
    logging.info("visualize_cluster_counts() completed successfully")

def visualize_nutrient_distribution():
    """
    Visualize distribution of key nutrients by cluster.
    args:        None
    returns:        None (saves output to PNG file) 
    """
    logging.info("visualize_nutrient_distribution() started")
# Load data
    df =pd.read_csv("data/models/clustering_results.csv")

    plt.figure(figsize=(10,6))
 # Boxplot of sugar distribution by cluster
    sns.boxplot(
        data=df,
        x="cluster_name" ,
        y="Total Sugars"
    )

    plt.title("Sugar Distribution by Cluster")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("data/outputs/sugar_distribution.png")
    plt.show()
    logging.info("Sugar distribution confirms sugary cereals have consistently higher sugar levels, while other clusters show wider variability.")
    logging.info("visualize_nutrient_distribution() completed successfully")

def run_visualizations():
    """
    Run all visualizations. This function calls each visualization function
    to illustrate the results of the clustering and trend analysis. The visualizations are saved for further analysis.
        returns:
            None (saves outputs to PNG files)
    """
    visualize_clusters()
    visualize_cluster_profiles()
    visualize_trend()
    visualize_cluster_heatmap()
    visualize_cluster_counts()
    visualize_nutrient_distribution()
    
   

if __name__ == "__main__":
    run_visualizations()

