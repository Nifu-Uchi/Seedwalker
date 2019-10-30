#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:22:18 2018

@author: hiro.t
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep
with open('deepurls.csv') as cs:
    urllist = list(csv.reader(cs))
for html in urllist:
    try:
        bsObj=BeautifulSoup(html,"lxml")#この行を実行後にエラーが出ます
        print("clear")
        sleep(0.1)
        break
    except RemoteDisconnected:
            print("error!!")
            sleep(0.2)
    print("")
