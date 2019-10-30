#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:47:47 2018

@author: hiro.t
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
APG_Clade_list=list()
APG_Order_list=list()
APG_Family_list=list()
Kew_Family_list=list()
Genus_list=list()
Species_Epithet_list=list()
Species_Author_list=list()



html=urlopen("http://data.kew.org/sid/SidServlet?ID=44632&Num=N98")
bsObj=BeautifulSoup(html,"lxml")
texx=bsObj.get_text()

tar="APG Clade: "
listn=APG_Clade_list
tex=texx
coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
listn.append(coll)
print(coll)  
    
    
