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
        linkslist.append(basedlink.attrs['href'])
print(linkslist)

for ids in linkslist:
    names = bsObj.findAll("a",{"href":ids})
    print(names)
    for name in names:
        nameslist.append(name.get_text())
        

weights=bsObj.findAll("span", {"style":"COLOR: navy"})
for weight in weights:
    weightlist.append(weight.get_text())


with open('test.csv','w') as F:
    for a,b,c in zip(nameslist,weightlist,linkslist):
        F.write('{},{},{}\n'.format(a,b,c))

    
    
