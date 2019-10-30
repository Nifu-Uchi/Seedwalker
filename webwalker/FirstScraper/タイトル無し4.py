from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html)
print(bsObj.findAll("a"))