from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load
from src.analysis.model_1 import run_model as model_1
from src.analysis.model_2 import run_model as model_2
from src.vis.visualizations import run_visualizations as visualize_clusters
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
#     data = extract()
#     print("running data extraction...\n")
#     if data:
#         print("Data extraction successful.\n")

#         for key, df in data.items():
#             print(f"{key} shape: {df.shape}")

#     else:
#         print("Data extraction failed.")
#         return


#     cereal_df, fmap_df = transform(data)

#     if cereal_df is not None and fmap_df is not None:
#         print("\nData transformation successful.")
#         print("Cereal DF shape:", cereal_df.shape)
#         print("FMAP DF shape:", fmap_df.shape)

#         print("\nCereal sample:")
#         print(cereal_df.head())

#         print("\nFMAP sample:")
#         print(fmap_df.head())

#     else:
#         print("Data transformation failed.")
    
#     load(cereal_df, fmap_df)
#     if cereal_df is not None and fmap_df is not None:
#         print("\nData loading successful.")
#     else:
#         print("Data loading failed.")
#         print("\nPipeline complete.")

#     print("Running cereal clustering model...\n")
#     model_1()
#     if model_1 is not None:
#         print("\nCereal clustering model completed successfully.")
#     else:
#         print("\nCereal clustering model failed.")

#     print("Running purchase trend model...\n")
#     model_2()
#     if model_2 is not None:
#         print("\nPurchase trend model completed successfully.")
#     else:
#         print("\nPurchase trend model failed.")

#     print("Running visualizations...\n")
#     visualize_clusters()
#     if visualize_clusters is not None:
#         print("\nVisualizations completed successfully.")
#     else:        
#         print("\nVisualizations failed.")

    try:
        logging.info("Starting pipeline")

        data = extract()
        if data is not None:
            logging.info("main.py Extract stage successful")    
        else:
            logging.error("main.py Extract stage failed")
            return

        cereal_df, fmap_df = transform(data)
        if cereal_df is not None and fmap_df is not None:
            logging.info("main.py Transform stage successful")      
        else:
            logging.error("main.py Transform stage failed")
            return

        load(cereal_df, fmap_df)
        if cereal_df is not None and fmap_df is not None:
            logging.info("main.py Load stage successful") 
        else:
            logging.error("main.py Load stage failed")
            return

        if extract and transform and load:
            logging.info("main.py ETL process completed successfully")
        else:
            logging.error("main.py ETL process failed")

        model_1()
        if model_1 is not None:
            logging.info("main.py Clustering model completed successfully")
        else:            
             logging.error("main.py Clustering model failed")

        model_2()
        if model_2 is not None:
            logging.info("main.py Trend model completed successfully")
        else:            
             logging.error("main.py Trend model failed")

        visualize_clusters()
        if visualize_clusters is not None:
            logging.info("main.py Visualizations completed successfully")
        else:            
             logging.error("main.py Visualizations failed")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")





    

if __name__ == "__main__":
    main()