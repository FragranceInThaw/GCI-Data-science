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

cols_to_use = [
    'MAL_ID', 'Name', 'Score', 'Genres', 'Type', 'Aired', 'Studios', 'Source','Members'
]
anime_data_extracted = anime_data[cols_to_use]
anime_data_extracted.head()
# 3.5 Practice
#　Let's examine the relationship between Score and Members in the anime_data_extracted dataset.
# Convert the Score column to type float first
anime_data_extracted = anime_data_extracted[anime_data_extracted["Score"] != "Unknown"].copy()
anime_data_extracted["Score"] = anime_data_extracted["Score"].astype(float)
scores = [0.0,6.0,7.5,8.5,10.0]
score_tier_names = ['Low','Average','High','Very High']
score_tiers = pd.cut(anime_data_extracted["Score"], scores, labels=score_tier_names)
popularity_tier_names = ['Niche','Moderate','Popular','Viral Hit']
popularity_tiers = pd.qcut(anime_data_extracted['Members'],4,labels=popularity_tier_names)

# Turns row categories into a full 2D table
pd.DataFrame({"Score": score_tiers, "Members": popularity_tiers}).value_counts().unstack()
print(pd.DataFrame({"Score": score_tiers, "Members": popularity_tiers}).value_counts().unstack())