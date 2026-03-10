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
    plt.savefig("data/models/cereal_cluster_scatter.png")
    plt.show()


def run_visualizations():
    """
    Run all visualizations. This function calls each visualization function (TO BE ADDED)
    to illustrate the results of the clustering and trend analysis. The visualizations are saved for further analysis.
        returns:
            None (saves outputs to PNG files)
    """

    visualize_clusters()



if __name__ == "__main__":
    run_visualizations()