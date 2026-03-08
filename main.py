from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load
from src.analysis.model_1 import run_model as model_1
from src.analysis.model_2 import run_model as model_2

def main():

    data = extract()

    if data:
        print("Data extraction successful.\n")

        for key, df in data.items():
            print(f"{key} shape: {df.shape}")

    else:
        print("Data extraction failed.")
        return


    cereal_df, fmap_df = transform(data)

    if cereal_df is not None and fmap_df is not None:
        print("\nData transformation successful.")
        print("Cereal DF shape:", cereal_df.shape)
        print("FMAP DF shape:", fmap_df.shape)

        print("\nCereal sample:")
        print(cereal_df.head())

        print("\nFMAP sample:")
        print(fmap_df.head())

    else:
        print("Data transformation failed.")
    
    load(cereal_df, fmap_df)
    if cereal_df is not None and fmap_df is not None:
        print("\nData loading successful.")
    else:
        print("Data loading failed.")

    # print("Running cereal clustering model...\n")
    # model_1()

    # print("Running purchase trend model...\n")
    # model_2()

    print("\nPipeline complete.")

    

if __name__ == "__main__":
    main()