from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep

html=urlopen("http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
linkslist=list()
for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
    if 'href' in basedlink.attrs:
        print(basedlink.attrs['href'])
        linkslist.append(basedlink.attrs['href'])
print("done")
print("___________________________")
print(linkslist)
for linkid in linkslist:
    
    html=("http://data.kew.org/sid/"+linkid)
    print(html)
    sleep(0.1)
    
    