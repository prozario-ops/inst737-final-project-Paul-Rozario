import pandas as pd
import os
from pathlib import  Path

def extract():
    project_root = Path(__file__).resolve().parents[2]
    data_dir= project_root / 'data'

    food= pd.read_csv(data_dir / 'food.csv', low_memory=False)
    branded_food= pd.read_csv(data_dir / 'branded_food.csv', low_memory=False)
    nutrient= pd.read_csv(data_dir / 'nutrient.csv', low_memory=False)

    fmap = pd.read_csv(data_dir / 'FMAP.csv', low_memory=False)

    nutrient_ids= [2047, 1003, 1004, 1005, 1063, 1079, 1089, 1087, 1093, 1092]

    chunks= []

    for chunk in pd.read_csv(
        data_dir/ "food_nutrient.csv", usecols= ['fdc_id', 'nutrient_id', 'amount'], 
        low_memory=False, chunksize= 200000
        ):
        filtered_chunk= chunk[chunk['nutrient_id'].isin(nutrient_ids)]
        chunks.append(filtered_chunk)
    food_nutrient= pd.concat(chunks, ignore_index=True)
    

    return {
        'food': food,
        'branded_food': branded_food,
        'nutrient': nutrient,
        'food_nutrient': food_nutrient,
        'fmap': fmap
    }
 



  