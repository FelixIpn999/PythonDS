from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd

url = "http://www.espn.com/nfl/statistics/team/_/stat/total"
html = urlopen(url)

soup = BeautifulSoup(html,"html.parser")
table = soup.find('tr',{"class":"colhead"})
print(table)