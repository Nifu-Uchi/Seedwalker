#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:13:41 2018

@author: hiro.t
"""

import csv
from bs4 import BeautifulSoup
import urllib.request
import re
from time import sleep
datacount=0
somea = list()


"""functions"""
def separator():    
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
               }

    response = urllib.request.urlopen(urllib.request.Request(url=urls, headers=headers))
    bsObj=BeautifulSoup(response,"lxml")
    result = bsObj.find(class_='gs_med')
    print("-----------1stres-----------")
    print(result)
    if result == None:
        print("some article")
        somea.append("")
        
    else:
        result2 = bsObj.find(class_='gs_red')
        print("-----------2ndres-----------")
        print(result2)
        if result2 == None:
            print("no aritcle")
            somea.append("n")
        else:
            print("some articles")
        
def writer():    
    with open("separated.csv",'a') as F:
        for a,b,c,d in zip(genuslist,
                           epitlist,
                           urllist,
                           somea):
            F.write('{},{},{},{}\n'.format(a,b,c,d))##csvファイルに保存
            
"""
functions over
"""


""""main"""

with open('urls.csv') as fp:
    urllist = list(csv.reader(fp))
    
with open('genuslist.csv') as fp:
    genuslist = list(csv.reader(fp))

with open('epitlist.csv') as fp:
    epitlist = list(csv.reader(fp))

for num in range(2,len(urllist)):
    urls=(((str(urllist[num])).replace("[","")).replace("]","")).replace("'","")
    separator()
    sleep(0.2)
    


    



