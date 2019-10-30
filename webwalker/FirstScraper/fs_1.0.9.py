#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:24:23 2018

@author: hiro.t
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://data.kew.org/sid/SidServlet?Clade=UNCERTAIN&Order=&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on")
bsObj=BeautifulSoup(html,"lxml")
linkslist=list()
nameslist=list()
weightlist=list()

weights=bsObj.findAll("span", {"style":"COLOR: navy"})
for weight in weights:
    weightlist.append(weight.get_text())

print(weightlist)


    

##
    
    
