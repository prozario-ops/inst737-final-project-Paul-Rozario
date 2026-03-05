import pandas as pd
import os
from pathlib import  Path

def extract():
    project_root = Path(__file__).resolve().parent

    raw_dir= project_root / 'data' / 'raw'

    food= pd.read_csv(raw_dir / 'food.csv')
    nutrient= pd.read_csv(raw_dir / 'nutrient.csv')
    food_nutrient= pd.read_csv(raw_dir / 'food_nutrient.csv')
    branded_food= pd.read_csv(raw_dir / 'branded_food.csv')

    fmap= pd.read_csv(raw_dir / 'fmap.csv')

    return {
        'food': food,
        'nutrient': nutrient,
        'food_nutrient': food_nutrient,
        'branded_food': branded_food,
        'fmap': fmap
    }




