# The following libraries are used, so please load them beforehand
import numpy as np
import numpy.random as random
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import os
import urllib.request
import zipfile
from io import StringIO
import io

# Visualization Library
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

# If this file is run in a Jupyter notebook, load the matplotlib extension.

# Displayed to 3 decimal places
np.set_printoptions(precision=3)

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
with urllib.request.urlopen(url) as response:
	archive_data = response.read()

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(archive_data))
z.extractall()

anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')
scores = [0.0,6.0,7.5,8.5,10.0]
score_tier_names = ['Low','Average','High','Very High']
cols_to_use = [
    'MAL_ID', 'Name', 'Score', 'Genres', 'Type', 'Aired', 'Studios', 'Source','Members'
]
anime_data_extracted = anime_data[cols_to_use]
anime_data_extracted.head()
# 3.6 Practice
#　Anime fans often joke that shows adapted from "Light Novels" have ridiculously long titles compared to original shows or manga. Let's see if this is true with anime_data_extracted. Group the dataset by Source and calculate the average (mean) Title_Length for each source type. Sort the results in descending order to see which source has the largest names.
# 
# Creates a new column named 'Title_Length' that will store the length of each anime
anime_data_extracted['Title_Length'] = anime_data_extracted['Name'].str.len()

anime_data_extracted.groupby('Source')['Title_Length'].mean()
print("Question 3.6: Which source has the largest average title length?")
print(anime_data_extracted.groupby('Source')['Title_Length'].mean().sort_values(ascending=False))