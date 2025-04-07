import pandas as pd

import matplotlib.pyplot as plt


data = pd.read_csv('netflix_titles.csv')


#there is not categories column so I assumed you meant type
# changes all null types entries to be 'unknown'
data['type'] = data['type'].where(data['type'].notnull(),'unknown')

#drops nan date values
data = data.dropna(subset=['date_added'])

#gets the amount of unique values in every single column
type_unique = data['type'].nunique()

title_unique = data['title'].nunique()

director_unique = data['director'].nunique()

cast_unique = data['cast'].nunique()

country_unique = data['country'].nunique()

date_added_unique = data['date_added'].nunique()


release_year_unique = data['release_year'].nunique()


rating_unique = data['rating'].nunique()

duration_unique = data['duration'].nunique()

listed_in_unique = data['listed_in'].nunique()

description_unique = data['description'].nunique()

#end of unqiue values 

#again movie type is not a column so I assume you mean movie versues tv show
most_frequent_movie_type = data['type'].value_counts().idxmax()


#oldest movie in the data
Oldest_entry = data[data['release_year'] == data['release_year'].min()]
#youngest movies plural in the database
youngests_entry = data[data['release_year'] == data['release_year'].max()]



#best year (2018)
best_year = data['release_year'].value_counts().idxmax()







