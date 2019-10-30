from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
linkslist=list()
nameslist=list()
weightlist=list()
for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
    if 'href' in basedlink.attrs:
        print(basedlink.attrs['href'])
        linkslist.append(basedlink.attrs['href'])
print(linkslist)

for ids in linkslist:
    names = bsObj.findAll("a",{"href":ids})
    print(names)
    for name in names:
        nameslist.append(name.get_text())
        
print(nameslist)

for weight in bsObj.findAll("SPAN",{"style":"COLOR: navy"}):
    weightlist.append(weight.get_text())
print(weightlist)
    

##
    
    
