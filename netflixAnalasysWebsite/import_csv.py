import os
import django
import pandas as pd
from datetime import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netflixAnalasysWebsite.settings")  
django.setup()

from searchPage.models import netflixData  


df = pd.read_csv('netflix_titles.csv')  


# Fill NaNs with empty string or suitable default
df = df.fillna('')

# Convert release_year (assumes it's just a year like 2018)
df['release_year'] = df['release_year'].apply(lambda x: datetime.strptime(str(int(x)), "%Y"))

# Convert rating and duration safely to integers
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)
df['duration'] = pd.to_numeric(df['duration'], errors='coerce').fillna(0).astype(int)


records = [
    netflixData(
        type=row['type'],
        title=row['title'],
        director=row['director'],
        cast=row['cast'],
        country=row['country'],
        date_added=row['date_added'],
        release_year=row['release_year'],
        rating=row['rating'],
        duration=row['duration'],
        listed_in=row['listed_in'],
        description=row['description'],
    )
    for _, row in df.iterrows()
]

netflixData.objects.bulk_create(records)
print(" CSV data imported successfully!")
