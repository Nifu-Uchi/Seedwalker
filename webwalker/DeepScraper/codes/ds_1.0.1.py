#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:16:52 2018

@author: hiro.t
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://data.kew.org/sid/SidServlet?ID=44632&Num=N98")
bsObj=BeautifulSoup(html,"lxml")
tex=bsObj.get_text()
target="APG Order: "
texts=re.findall(target+"(.*)",tex)
print(texts)