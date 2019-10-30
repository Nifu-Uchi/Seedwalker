#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:16:52 2018

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

texts=bsObj.get_text

print(text)