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
# 3.4 Practice
#　Using the data from <Exercise 3-3>, let's vertically join the following data for df4.
data4 = {
    'id':['0','1','2','3','4','6','8','11','12','13'],
    'city':['Tokyo','Osaka','Kyoto','Hokkaido','Tokyo','Tokyo','Osaka','Kyoto','Hokkaido','Tokyo'],
    'birth_year':[1990,1989,1992,1997,1982,1991,1988,1990,1995,1981],
    'name':['Hiroshi','Akiko','Yuki','Satoru','Steeve','Mituru','Aoi','Tarou','Suguru','Mitsuo']
}
df4 = DataFrame(data4)
print(df4)

# Prepare data 5
data5 = {
    'id':['0','1','3','6','8'],
    'math':[20,30,50,70,90],
    'English':[30,50,50,70,20],
    'sex':['M','F','F','M','M'],
    'index_num':[0,1,2,3,4]
}
# Preparing data
hier_df1 = DataFrame(
    np.arange(12).reshape((3,4)),
    index = [['c','d','d'], [1,2,1]],
    columns = [
        ['Kyoto','Nagoya','Hokkaido','Kyoto'],
        ['Yellow','Yellow','Red','Blue']
    ]
)

hier_df1.index.names = ['key1','key2']
hier_df1.columns.names = ['city','color']
hier_df1
df5 = DataFrame(data5)
print(df5)
print("Question 3.4: Using the data from <Exercise 3-3>, let's vertically join the following data for df4.")
print(pd.concat([df4, df5], ignore_index=True))