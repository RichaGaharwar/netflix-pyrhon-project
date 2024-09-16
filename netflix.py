# """Netflix Python libraries.ipynb

# Original file is located at
#     https://colab.research.google.com/drive/1aWdlCfXbAYIdFc7v_34SLPX-qt4oUv6A """



from google.colab import files
uploaded = files.upload()

import pandas as pd
netflix_titles = pd.read_csv('netflix_titles.csv')

# """Find the counts of each categorical variable both using graphical and nongraphical analysis.
# a. For Non-graphical Analysis:"""

import pandas as pd
type_counts = netflix_titles['type'].value_counts()
print(type_counts)

# """b. For graphical analysis:"""

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
sns.countplot(data=netflix_titles, x='type')
plt.title('Counts of Each Category in Type Column')
plt.show()

# """Comparison of tv shows vs. movies.
# a. Find the number of movies produced in each country and pick the top 10
# countries."""

import pandas as pd
movies_df = netflix_titles[netflix_titles['type'] == 'Movie']
movie_counts_by_country = movies_df.groupby('country')['title'].nunique()
top_10_countries = movie_counts_by_country.sort_values(ascending=False).head(10)
print(top_10_countries)

# """b. Find the number of Tv-Shows produced in each country and pick the top 10
# countries."""

import pandas as pd
tv_shows_df = netflix_titles[netflix_titles['type'] == 'TV Show']
tv_show_counts_by_country = tv_shows_df.groupby('country')['title'].nunique()
top_10_countries_tv_shows = tv_show_counts_by_country.sort_values(ascending=False).head(10)
print(top_10_countries_tv_shows)

# """ Find which is the best week to release the Tv-show or the movie."""

import pandas as pd
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'])
netflix_titles['week_added'] = netflix_titles['date_added'].dt.strftime('%U')
movies_df = netflix_titles[netflix_titles['type'] == 'Movie']
tv_shows_df = netflix_titles[netflix_titles['type'] == 'TV Show']
movies_by_week = movies_df.groupby('week_added')['title'].count()
tv_shows_by_week = tv_shows_df.groupby('week_added')['title'].count()
best_week_for_movies = movies_by_week.idxmax()
best_week_for_tv_shows = tv_shows_by_week.idxmax()
print("Best Week for Movies:", best_week_for_movies)
print("Best Week for TV Shows:", best_week_for_tv_shows)

# """a. What is the best time to launch a TV show?"""

import pandas as pd
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'])
netflix_titles['month_added'] = netflix_titles['date_added'].dt.strftime('%B')
movies_df = netflix_titles[netflix_titles['type'] == 'Movie']
movies_by_month = movies_df.groupby('month_added')['title'].count()
best_month_for_movies = movies_by_month.idxmax()
print("Best Month for Movie Releases:", best_month_for_movies)

# """b. Find which is the best month to release the Tv-show or the movie. Do the
# analysis separately for Tv-shows and Movies"""

import pandas as pd
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'])
netflix_titles['month_added'] = netflix_titles['date_added'].dt.month_name()
tv_shows_df = netflix_titles[netflix_titles['type'] == 'TV Show']
tv_shows_by_month = tv_shows_df.groupby('month_added')['title'].count()
best_month_for_tv_shows = tv_shows_by_month.idxmax()
print("Best Month for TV Show Releases:", best_month_for_tv_shows)

# """Identify the top 10 directors who have appeared in most movies or TV shows"""

import pandas as pd
movies_and_tv_shows_df = netflix_titles[(netflix_titles['type'] == 'Movie') | (netflix_titles['type'] == 'TV Show')]
director_counts = movies_and_tv_shows_df.groupby('director')['title'].nunique()
top_10_directors = director_counts.sort_values(ascending=False).head(10)
print(top_10_directors)

# """Identify the top 10 actors who have appeared in most movies or TV shows"""

import pandas as pd
movies_and_tv_shows_df = netflix_titles[(netflix_titles['type'] == 'Movie') | (netflix_titles['type'] == 'TV Show')]
director_counts = movies_and_tv_shows_df.groupby('actor')['title'].nunique()
top_10_directors = director_counts.sort_values(ascending=False).head(10)
print(top_10_actors)

# """Which genre movies are more popular or produced more"""

# !pip install wordcloud

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(netflix_titles['listed_in']))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Movie Genre Word Cloud')
plt.show()

# """Find After how many days the movie will be added to Netflix after the release of the movie"""

import pandas as pd
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'])
netflix_titles['days_to_add'] = (netflix_titles['date_added'] - pd.to_datetime(netflix_titles['release_year'], format='%Y')).dt.days
mode_days_to_add = netflix_titles['days_to_add'].mode().values[0]
print("Mode of Days to Add:", mode_days_to_add)