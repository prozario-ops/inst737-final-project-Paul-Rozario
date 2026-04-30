import pandas as pd
import os
from pathlib import  Path
import logging

def extract():
    """
    extract() reads the raw CSV files from the data directory and loads them into pandas DataFrames.

    Returns:
        dict: A dictionary containing the loaded DataFrames for 'food', 'branded_food', 'nutrient', 'food_nutrient', and 'fmap'.
    
    """
    logging.info("extract.py extract() started")

    try:
        # set project root and data directory
        project_root = Path(__file__).resolve().parents[2]
        data_dir= project_root / 'data/raw'
        # read CSV files into DataFrames
        food= pd.read_csv(data_dir / 'food.csv', low_memory=False)
        branded_food= pd.read_csv(data_dir / 'branded_food.csv', low_memory=False)
        nutrient= pd.read_csv(data_dir / 'nutrient.csv', low_memory=False)
        fmap = pd.read_csv(data_dir / 'FMAP.csv', low_memory=False)
        # food_nutrient can be large, so we read it in chunks and filter for relevant nutrients
        nutrient_ids= [2047, 1003, 1004, 1005, 2000, 1079, 1089, 1087, 1093, 1092]

        chunks= []

        for chunk in pd.read_csv(
            data_dir/ "food_nutrient.csv", usecols= ['fdc_id', 'nutrient_id', 'amount'], 
            low_memory=False, chunksize= 200000
            ):
            filtered_chunk= chunk[chunk['nutrient_id'].isin(nutrient_ids)]
            chunks.append(filtered_chunk)
        food_nutrient= pd.concat(chunks, ignore_index=True)
        
        # return all loaded DataFrames in a dictionary
        if food is not None and branded_food is not None and nutrient is not None and food_nutrient is not None and fmap is not None:
            logging.info("extract.py executed successfully")
        else:
            logging.error("extract.py failed to load all datasets")
        return {
            'food': food,
            'branded_food': branded_food,
            'nutrient': nutrient,
            'food_nutrient': food_nutrient,
            'fmap': fmap
        }
        
        
    except Exception as e:
        logging.error(f"Error during extraction: {e}")
        return None
 



  