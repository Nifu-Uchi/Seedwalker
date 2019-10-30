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
maxduetime=10
maxedduetime=0

print(urllist)
def checkers():
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    print("finishedurl"+str(fin))
    start=amount-fin
    st=fin+1
    
    if start >= 100:
        print("good")
        for num in range(99):
            listnum=int(num+fin+1)
            print(urllist[listnum])
       
        file = open('finishedurl.txt', 'w')  #書き込みモードでオープン
        string = str(fin+100)
        file.write(string)
        
    else:
        print("less")
        for num in range(int(st)):
            print(list(num+fin+1))
        maxedduetime=1

for cal in range(maxduetime):
    if maxedduetime == 1:
        print("fininished")
    else:
        checkers()
        
        
        

    


