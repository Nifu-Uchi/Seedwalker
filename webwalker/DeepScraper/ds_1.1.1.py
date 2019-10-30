#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:05:38 2018

@author: hiro.t
"""


import csv
with open('test.csv') as fp:
    urllist = list(csv.reader(fp))
duetime=0
maxduetime=10
maxedduetime=0
print(urllist)

url=open("urlnumber.txt").read()
amount=float(url)
finurl=open("finishedurl.txt").read()
fin=int(finurl)
start=amount-fin
