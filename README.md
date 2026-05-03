# inst737-final-project-Paul-Rozario


# Cereal Market Analytics Pipeline


## Project Overview


This project builds an end-to-end data analytics pipeline to analyze cereal products from both a nutritional and consumer purchasing perspective. The goal is to demonstrate how data science techniques can support grocery retailers in understanding cereal market trends and making better assortment decisions.


### Business Problem


Cereal consumption in the United States has been declining as consumer preferences shift toward healthier or more protein-focused food options. Grocery retailers must decide which cereal products to stock, how to position them within stores, and whether cereals should remain a major product category.


The business problem this project aims to address is how grocery stores can use data analytics to understand consumer preferences to predict cereal assortments. By identifying distinct nutritional groupings and examining broader purchasing trends from USDA datasets, these insights can inform decisions around product assortment, shelf placement, and category strategy.


### Data Sets Used


This project uses two primary datasets from U.S. government sources.


1. **USDA FoodData Central – Branded Foods (December 2025)**
   - Nutritional information for cereal products
   - Features include:
     - Protein
     - Total lipids (fat)
     - Carbohydrates
     - Total sugars
     - Fiber
     - Sodium (handled carefully due to extreme outliers)
     - serving_size_grams (for heatmap)


2. **USDA ERS Food-at-Home Monthly Area Prices (F-MAP) (Current Data: 2012-2018)**
   - Monthly price and purchase information for food-at-home categories.
   - Captures broader consumer purchasing behavior and price dynamics across regions
   - Used to model and visualize cereal purchasing trends


*  **RAW data description (CSV)**
   - branded_food.csv – Contains product-level metadata for branded food items in the USDA FoodData Central database, including brand information, product descriptions, and serving size details.


   - FMAP.csv – Contains USDA Economic Research Service Food-at-Home Monthly Area Prices data, providing regional cereal purchasing and pricing trends over time.


   - food_nutrient.csv – Stores nutrient quantities for each food item, linking food records to specific nutrients and their measured values.


   - food.csv – Provides general metadata for food items in the FoodData Central database, including identifiers and basic classification information.


   - nutrient.csv – Contains reference information for nutrients, including nutrient names, units of measurement, and nutrient  identifiers used in the dataset.


Together, these datasets allow the project to analyze:


* **Product attributes** (nutrition profiles)
* **Consumer purchasing behavior** (spending trends)


### Techniques Employed


Several data science and analytics techniques are used throughout the project.


**Data Engineering**


* ETL pipeline (Extract, Transform, Load)
* Data cleaning and filtering
* Feature selection
* Reshaping data from long to wide format
* Handling large datasets via chunking


**Machine Learning**


* K-Means clustering to group cereals based on nutritional characteristics
* Cluster evaluation using silhouette score


**Time Series Analysis**


* Linear regression trend modeling to analyze cereal purchasing behavior over time
* Evaluation using R² and RMSE


**Data Visualization**


* Scatter plots of cereal nutrition clusters
* Nutritional heatmaps by cluster
* Time-series trend charts


## Setup Instructions


Follow these steps to run the project locally.


### 1. Clone the Repository


```bash
git clone https://github.com/prozario-ops/inst737-final-project-Paul-Rozario.git
cd inst737-final-project-Paul-Rozario
```

### 2. Create a Virtual Environment


```bash
python -m venv venv

```
depending on your interpreter, may have to do this instead:

```bash
py -m venv venv

```

### 3. Activate the Virtual Environment


**Windows**


```bash
venv\Scripts\activate
```


**Mac / Linux**


```bash
source venv/bin/activate
```


### 4. Install Dependencies


```bash
pip install -r requirements.txt
```
NOTE: this may take a few minutes.


The project uses the following Python libraries:


* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn


---


## Running the Project


### Run the Data Pipeline


The main pipeline script executes all stages of the project.


```bash
python main.py
```
OR, depending on your interpreter:

```bash
py main.py
```

Running the pipeline will:


1. Extract raw cereal nutrition data
2. Transform and clean the dataset
3. Build clustering models
4. Perform purchasing trend analysis
5. Generate visualizations
6. Save model outputs to the data directory

View pipeline progress in pipeline.log
---




## Code Package Structure


```
inst737-final-project-Paul-Rozario/


README.md
requirements.txt
main.py
pipeline.log


src/
    analysis/
    etl/
        extract.py
        transform_load.py
        model_clusters.py
        model_trends.py
        visualize.py


data/
    raw/
        branded_food.csv
        FMAP.csv
        food_nutrient.csv
        food.csv
        nutrient.csv
    processed/
        transform.py cereal_nutrients.csv
        transform.py FMAP cereal_price_timeseries
    models/
        model_1.py csv (using processed csv)
        model_2.py csv (using processed csv)
        model_evaluation/
                clustering_evaluation.csv
                trend_evaluation.csv
    outputs/
        cereal_cluster_heatmap.png
        cereal_cluster_scatter.png
        cereal_trend.png
        protein_cluster_bar.png
        cluster_counts.png
        sugar_distribution.png
```


### Folder Descriptions


**src/**
Contains the core pipeline modules.


* `extract.py` – Extracts raw data
* `transform_load.py` – Cleans and transforms datasets
* `model_1.py` – Performs K-Means clustering on cereal nutrition data and cluster evaluation using silhouette score
* `model_2.py` – Builds regression model for purchase trends and trend evaluation using R2/RMSE
* `visualize.py` – Generates plots and heatmaps


---


**data/**


* `raw/`Original downloaded datasets
* `processed/` – Cleaned datasets produced during the ETL stage
* `models/` – Model outputs and predictions used for visualization
* `outputs/` – Visualization outputs


---


## Example Outputs


The project generates several visualizations that summarize the analytical findings.


**Cereal Nutrition Clusters**


A scatter plot showing how cereal products cluster based on protein and sugar content.


**Average Nutrient Profile Heatmap**


A heatmap summarizing the average nutritional composition of each cereal cluster.


**Cereal Purchasing Trend Over Time**


A time-series visualization showing overall cereal purchasing trends across multiple years.

**Cluster Cereal Counts**

A barplot that shows the amount of cereals per cluster.

**Sugar Nutrient distribution across clusters**

A boxplot that to visualize how sugar is distributed across clusters


---


## Technologies Used


* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn


---


## Author


Paul Rozario
INST737 – Data Science Project
