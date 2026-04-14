import logging
from pathlib import Path


def load(cereal_df, fmap_df):
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

        print("\nData successfully saved:")
        print(f"Cereal dataset - {cereal_path}")
        print(f"FMAP dataset - {fmap_path}")
        if cereal_df is not None and fmap_df is not None:
            logging.info("load.py executed successfully")
        else:
            logging.error("load.py failed to save datasets")
        
    except Exception as e:
        print(f"Error saving data: {e}")
        raise