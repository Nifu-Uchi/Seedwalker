#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:13:41 2018

@author: hiro.t
"""
import sys

print(sys.version)

from bs4 import BeautifulSoup
import urllib.request
import re
from time import sleep

url = "https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=sssssssssaereadsafsss+self&btnG="
urls ="https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&q=Buphthalmum+salicifolium+self+compatibility&btnG="
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
bsObj=BeautifulSoup(response,"lxml")
result = bsObj.find(class_='gs_med')
print(result)
if result == None:
    print("some article")
else:
    print("no aritcle")

    
