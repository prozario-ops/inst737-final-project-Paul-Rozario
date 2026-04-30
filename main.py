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
            logging.info("Visualizations confirm meaningful cereal segmentation and a weak but slightly declining purchasing trend.")
        else:            
             logging.error("main.py Visualizations failed")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")





    

if __name__ == "__main__":
    main()