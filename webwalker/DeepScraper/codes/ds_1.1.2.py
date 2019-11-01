#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:26:32 2018

@author: hiro.t
"""

import csv
with open('test.csv') as fp:
    urllist = list(csv.reader(fp))
duetime=0
maxduetime=3
maxedduetime=0
amounturl_list=list()
print(urllist)
def checkers():
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    print("finishedurl"+str(fin))
    start=amount-fin
    if start >= 100:
        print("good")
        truelist=urllist[int(fin):int(fin+100)]
        getting=list(truelist)
        print(getting)
        file = open('finishedurl.txt', 'w')  #書き込みモードでオープン
        string = str(fin+100)
        file.write(string)
        
    else:
        print("less")
        truelist=urllist[int(fin):]
        getting=list(truelist)
        print(getting)
        file = open('finishedurl.txt', 'w')  #書き込みモードでオープン
        string = str(amount)
        file.write(string)
        maxedduetime="fin"
    amounturl_list.append(truelist)        
for cal in range(maxduetime):
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    if fin == amount:
        print("fininished")
    else:
        checkers()
        
open("dates.csv",'w')
with open('dates.csv', 'a', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(amounturl_list)
        
        
        

    


