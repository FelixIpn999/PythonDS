"""import numpy as np
from sklearn import preprocessing

data =  np.array([[3,-1.5,2,-5.4],[0,4,-0.3,2.1],[1,3.3,-1.9,-4.3]])

data_standarized = preprocessing.scale(data)
print("Mean ",data_standarized.mean(axis=0))
print("Standard desviation ",data_standarized.std(axis=0))"""

from bs4 import BeautifulSoup
import urllib.request 

url = "http://www.nfl.com/stats/categorystats?tabSeq=2&offensiveStatisticCategory=GAME_STATS&conference=ALL&role=TM&season=2016&seasonType=REG&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=2&d-447263-n=1"
