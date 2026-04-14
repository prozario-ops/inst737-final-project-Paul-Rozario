import pandas as pd
import logging


def transform(data):
    """
    transform() takes the extracted DataFrames and processes them to create two cleaned datasets:

    args:
        data (dict): A dictionary containing the raw DataFrames for 'food', 'branded_food', 'nutrient', 'food_nutrient', and 'fmap'.
        
    returns:
        cereal_df (pd.DataFrame): A DataFrame containing nutrient information for cereal foods, merged with descriptions and branded food metadata.
        fmap_df (pd.DataFrame): A DataFrame containing the FMAP price timeseries data, with a proper date column.
    """
    try:
        food = data["food"]
        branded_food = data["branded_food"]
        nutrient = data["nutrient"]
        food_nutrient = data["food_nutrient"]
        fmap = data["fmap"]

    
        # Filter cereal foods
    

        cereal_food = food[
            food["description"].str.contains("cereal", case=False, na=False)
        ]

        cereal_ids = cereal_food["fdc_id"].unique()

    
        # Filter nutrients for those cereals
        

        food_nutrient = food_nutrient[
            food_nutrient["fdc_id"].isin(cereal_ids)
        ]

        
        # Nutrients of interest (by ID)
    

        nutrient_ids = [
            2047,  # Energy
            1003,  # Protein
            1004,  # Fat
            1005,  # Carbohydrate
            2000,  # Sugar
            1079,  # Fiber
            1089,  # Iron
            1087,  # Calcium
            1093,  # Sodium
            1092   # Potassium
        ]

        food_nutrient = food_nutrient[
            food_nutrient["nutrient_id"].isin(nutrient_ids)
        ]

        # Pivot nutrients (using nutrient_id)
        

        cereal_nutrients = food_nutrient.pivot_table(
            index="fdc_id",
            columns="nutrient_id",
            values="amount",
            aggfunc="mean"
        ).reset_index()

        
        # Rename nutrient columns

        cereal_nutrients = cereal_nutrients.rename(columns={
            2047: "Energy",
            1003: "Protein",
            1004: "Total lipid (fat)",
            1005: "Carbohydrate",
            2000: "Total Sugars",
            1079: "Fiber",
            1089: "Iron",
            1087: "Calcium",
            1093: "Sodium",
            1092: "Potassium"
        })

        
        # 6. Merge cereal descriptions
    

        cereal_df = cereal_nutrients.merge(
            cereal_food[["fdc_id", "description"]],
            on="fdc_id",
            how="left"
        )

        # 7. Merge branded food metadata
    

        cereal_df = cereal_df.merge(
            branded_food[
                [
                    "fdc_id",
                    "brand_owner",
                    "brand_name",
                    "serving_size_grams",
                    "branded_food_category"
                ]
            ],
            on="fdc_id",
            how="left"
        )

        
        # 8. FMAP transformation
        

        fmap["date"] = pd.to_datetime(
            fmap["Year"].astype(int).astype(str)
            + "-"
            + fmap["Month"].astype(int).astype(str)
        )

        fmap_df = fmap[
            [
                "Year",
                "Month",
                "Unit_value_mean_wtd",
                "Price_index_GEKS",
                "Purchase_dollars_wtd",
                "Purchase_grams_wtd",
                "date",
            ]
        ]
        if cereal_df is not None and fmap_df is not None:
            logging.info("transform.py executed successfully")
        elif cereal_df is None:
            logging.error("transform.py failed to create cereal_df")
        elif fmap_df is None:
            logging.error("transform.py failed to create fmap_df")
        
        return cereal_df, fmap_df
        
    except Exception as e: 
        print(f"Error in transformation: {e}")
        raise
