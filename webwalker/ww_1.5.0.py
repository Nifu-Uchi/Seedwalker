from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
linkslist=list("l")
nameslist=list("n")
weightlist=list()
for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
    if 'href' in basedlink.attrs:
        print(basedlink.attrs['href'])
        urlid=basedlink.attrs['href']
        url="http://data.kew.org/sid/"+urlid
        
        linkslist.append(url)
print(linkslist)


with open('deepurls.csv','w') as F:
    for a in zip(linkslist):
        F.write('{}\n'.format(a))

    
    
