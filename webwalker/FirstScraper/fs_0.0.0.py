from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://data.kew.org/sid/SidServlet?Clade=COMMELINOIDS&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj = BeautifulSoup(html, "html.parser")
print("printing...")
print(bsObj.h2)
print("done")
