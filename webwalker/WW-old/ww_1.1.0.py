#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:56:02 2018

@author: hiro.t
"""
#初期設定
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep
html=urlopen("http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
linkslist=list("l")
nameslist=list("n")
weightlist=list()
htmllist=list("h")
a="aa"

##idを取得
print("==get id_start==" )
for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
    if 'href' in basedlink.attrs:
        linkslist.append(basedlink.attrs['href'])

for linkid in linkslist:    
    print("http://data.kew.org/sid/"+linkid)
    htmllist.append("http://data.kew.org/sid/"+linkid)
   

print("==get id_end==" )
##名前を取得
print("==get name_start==" )
for ids in linkslist:
    names = bsObj.findAll("a",{"href":ids})
    print(names)
    for name in names:
        nameslist.append(name.get_text())
        print(name)
        sleep(0.01)
print("==get name_end==" )        
##重さを取得
print("==get weight_start==" ) 
weights=bsObj.findAll("span", {"style":"COLOR: navy"})
for weight in weights:
    weightlist.append((weight.get_text()).replace("g",""))##gを取り除いてリスト化
    print((weight.get_text()).replace("g",""))
    
print("==get weight_end==" ) 
##一覧を保存
print("==write csv==" ) 
with open("{a}.csv",'w') as F:
    for a,b,c in zip(nameslist,weightlist,htmllist):
        F.write('{},{},{}\n'.format(a,b,c))

    
    
