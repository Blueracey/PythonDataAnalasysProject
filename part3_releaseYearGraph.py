import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('netflix_titles.csv')


year_data = data['release_year'].dropna()

plt.hist(year_data, bins=range(int(year_data.min()), int(year_data.max()) ), color='salmon', edgecolor='black')





plt.show()