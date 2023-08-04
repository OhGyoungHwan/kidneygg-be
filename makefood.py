from food.models import Food
from food.serializers import FoodSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import pandas as pd

foodpd = pd.read_csv('./food.csv')

for id,row in foodpd.iterrows():
    food = Food(no=id,name=row['name'],categorie=row["categorie"],energy=row["energy"],moisture=row["moisture"],protein=row["protein"],phosphorus=row["phosphorus"],potassium=row["potassium"],natrium=row["natrium"])
    food.save()
    