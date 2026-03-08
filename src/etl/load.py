from pathlib import Path


def load(cereal_df, fmap_df):

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