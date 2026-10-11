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

anime_data_extracted = anime_data_extracted[anime_data_extracted["Score"] != "Unknown"].copy()
anime_data_extracted["Score"] = anime_data_extracted["Score"].astype(float)
# 3.8 Practice
#　Missing Data: Let's investigate the different animation studios. Group the dataset by Studios and calculate the mean, max, and count of Score for each studio. Sort the results in descending order to see which studio has the highest average score.
# 
anime_data = anime_data.replace('Unknown', np.nan)
cols_to_use2 = [
    "Name", "Score", "Type", "Premiered", "Studios", "Source",
]
anime_data_extracted_pracq = anime_data[cols_to_use2]
anime_data_extracted_pracq["Score"] = anime_data_extracted_pracq["Score"].astype(float)
anime_data_extracted_dropna = anime_data_extracted_pracq.dropna()
anime_data_extracted_dropna["Score"].mean()
anime_data_extracted_filln1 = anime_data_extracted_pracq.fillna(-1)
anime_data_extracted_filln1["Score"].mean()
anime_data_extracted_fillmean = anime_data_extracted_pracq.fillna(anime_data_extracted_pracq["Score"].mean())
anime_data_extracted_fillmean["Score"].mean()
print("Question 3.8: Which studio has the highest average score?")
print(anime_data_extracted_dropna.groupby("Studios")["Score"].mean().sort_values(ascending=False).head(10))
