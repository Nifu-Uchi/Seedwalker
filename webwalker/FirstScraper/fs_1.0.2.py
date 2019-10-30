from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://data.kew.org/sid/SidServlet?Clade=COMMELINOIDS&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj = BeautifulSoup(html, "html.parser")

    
    
names = bsObj.findAll("A HREF",{"SidServlet?ID=56460&Num=eXI"})
for name in names:
    print(name.get_text())
