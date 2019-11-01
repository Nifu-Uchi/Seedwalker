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
counter=0
def lister(urls):
    int(counter)
    print("Count."+str(counter))
    print("accessing  "+urls)
    html=urlopen(urls)
    bsObj=BeautifulSoup(html,"lxml")
    print("accessed!")
    sleep(0.5)
    linkslist=list()
    nameslist=list()
    weightlist=list()
    htmllist=list()
    nameslist.append("name")
    htmllist.append("URL")
    cate=(urls.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")
    print("========="+cate+"list START!")
    sleep(1)

    ##idを取得
    print("==get id_start==")
    sleep(1)
    for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
        if 'href' in basedlink.attrs:
            linkslist.append(basedlink.attrs['href'])

    for linkid in linkslist:    
        print("http://data.kew.org/sid/"+linkid)
        htmllist.append("http://data.kew.org/sid/"+linkid)
        
   
    print("get"+str(len(htmllist))+"urls")
    print("==get id_end==" )
    
    ##名前を取得
    print("==get name_start==" )
    sleep(1)
    
    for ids in linkslist:
        names = bsObj.findAll("a",{"href":ids})
        for name in names:
            nameslist.append(name.get_text())
            print(name.get_text())
        bsObj=bsObj.replace("<A HREF="+ids+"*""A>","")
           
    print("get"+str(len(nameslist)))
    print("==get name_end==" )        
    ##重さを取得
    print("==get weight_start==" ) 
    sleep(1)
    weights=bsObj.findAll("span", {"style":"COLOR: navy"})
    for weight in weights:
        weightlist.append((weight.get_text()).replace("g",""))##gを取り除いてリスト化
        print((weight.get_text()).replace("g",""))
        
        print("==get weight_end==" )
    print("get"+str(len(weightlist)))
    ##一覧を保存
    print("==write csv==" ) 
    sleep(1)
    with open(cate+".csv",'w') as F:
        for a,b,c in zip(nameslist,weightlist,htmllist):
            F.write('{},{},{}\n'.format(a,b,c))

    print("========="+cate+"list DONE!")
    sleep(1)
    
    
urllist=list(open("urls.txt"))
for geturl in urllist:
    print(geturl)
print(str(len(urllist))+"URL is here")
sleep(1)
print("Process is starting..........")
print("")
for sites in urllist:
    counter=counter+1
    lister(sites)
    print(sites+"is done")
print("done")
