#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:48:01 2018

@author: hiro.t
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://data.kew.org/sid/SidServlet?ID=58210&Num=58v")
source=BeautifulSoup(html,"lxml")
print(source)
a = re.search("Species Author*br$",source).group()
print(a)