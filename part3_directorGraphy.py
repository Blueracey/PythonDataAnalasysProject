import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('netflix_titles.csv')




Director_review = data['director'].value_counts()


#displays the top 10 directors 
Director_review.head(10).plot(kind='bar')


plt.show()