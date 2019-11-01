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

def lister(urls):
    html=urlopen(urls)
    bsObj=BeautifulSoup(html,"lxml")
    linkslist=list()
    nameslist=list()
    weightlist=list()
    htmllist=list()
    nameslist.append("name")
    htmllist.append("URL")
    cate=(urls.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")


    ##idを取得
    print("==get id_start==")
    sleep(1)
    for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
        if 'href' in basedlink.attrs:
            linkslist.append(basedlink.attrs['href'])

    for linkid in linkslist:    
        print("http://data.kew.org/sid/"+linkid)
        htmllist.append("http://data.kew.org/sid/"+linkid)
        sleep(0.01)
   
    print("get"+len(linkid)+"urls")
    print("==get id_end==" )
    
    ##名前を取得
    print("==get name_start==" )
    sleep(1)
    
    for ids in linkslist:
        names = bsObj.findAll("a",{"href":ids})
        for name in names:
            nameslist.append(name.get_text())
            print(name.get_text())
            sleep(0.01)
    print("get"+len(name))
    print("==get name_end==" )        
    ##重さを取得
    print("==get weight_start==" ) 
    sleep(1)
    weights=bsObj.findAll("span", {"style":"COLOR: navy"})
    for weight in weights:
        weightlist.append((weight.get_text()).replace("g",""))##gを取り除いてリスト化
        print((weight.get_text()).replace("g",""))
        sleep(0.01)
        print("==get weight_end==" )
    print("get"+len(weight))
    ##一覧を保存
    print("==write csv==" ) 
    sleep(1)
    with open(cate+".csv",'w') as F:
        for a,b,c in zip(nameslist,weightlist,htmllist):
            F.write('{},{},{}\n'.format(a,b,c))

    print("========="+cate+"list DONE!")
    sleep(1)
    
    
urllist=open("urls.txt")

for sites in urllist:
    lister(sites)
    print(sites+"is done")
