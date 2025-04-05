import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('netflix_titles.csv')



country_counts = data['country'].value_counts()



#creates a bar chart 
country_counts.head(20).plot(kind='bar')


plt.show()