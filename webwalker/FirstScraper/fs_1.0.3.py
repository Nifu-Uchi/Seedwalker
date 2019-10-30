from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://data.kew.org/sid/SidServlet?Clade=COMMELINOIDS&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
    if 'href' in basedlink.attrs:
        print(basedlink.attrs['href'])
        

