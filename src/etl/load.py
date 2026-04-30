import logging
from pathlib import Path


def load(cereal_df, fmap_df):
    """
    load() saves the processed cereal nutrient dataset and FMAP price timeseries dataset to CSV files in the data/processed directory.
    args:
        cereal_df (pd.DataFrame): The processed cereal nutrient dataset.
        fmap_df (pd.DataFrame): The processed FMAP price timeseries dataset.
    
    returns:
        None (saves outputs to CSV files)
    """
    logging.info("load.py load() started")

    try:
        # Create processed data directory
        processed_dir = Path("data/processed")
        processed_dir.mkdir(parents=True, exist_ok=True)

        # File paths
        cereal_path = processed_dir / "cereal_nutrients.csv"
        fmap_path = processed_dir / "cereal_price_timeseries.csv"

        # Save datasets
        cereal_df.to_csv(cereal_path, index=False)
        fmap_df.to_csv(fmap_path, index=False)

        logging.info("\nData successfully saved:")
        logging.info(f"Cereal dataset - {cereal_path}")
        logging.info(f"FMAP dataset - {fmap_path}")
        if cereal_df is not None and fmap_df is not None:
            logging.info("load.py executed successfully")
        else:
            logging.error("load.py failed to save datasets")
        
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        raise