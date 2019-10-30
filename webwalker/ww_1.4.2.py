#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:26:32 2018

@author: hiro.t
"""

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep

APG_Clade_list=list()
APG_Order_list=list()
APG_Family_list=list()
Kew_Family_list=list()
Genus_list=list()
Species_Epithet_list=list()
Species_Author_list=list()
Weight_list=list()
counter=0
def nocheck(col0):
    global coll
    if col0 != None:
        coll=(col0.group(1)).replace(",","★")
    else:

        coll="NONE"


tar=""
def collector(URL):
    html=urlopen(URL)
    bsObj=BeautifulSoup(html,"lxml")
    tex=bsObj.get_text()
    
    

    tar="APG Clade: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    APG_Clade_list.append(coll)
    print(coll)
    
    tar="APG Order: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    APG_Order_list.append(coll)
    print(coll) 
    
    tar="APG Family: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    APG_Family_list.append(coll)
    print(coll) 
    
    tar="Kew Family: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    Kew_Family_list.append(coll)
    print(coll)
    
    tar="Genus: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    Genus_list.append(coll)
    print(coll) 
    
    tar="Species Epithet: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    Species_Epithet_list.append(coll)
    print(coll) 
    
    tar="Species Author: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    Species_Author_list.append(coll)
    print(coll) 

    tar="Average 1000 Seed Weight.*: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)
    Weight_list.append(coll)
    print(coll) 
    
    
        


def getter(urlname):
    global counter
    counter=counter+1
    print("--"+str(counter)+"count URL---")
    collector(urlname)
    print("----")
    
    
def writer():    
    with open(str(counter)+"splist.csv",'a') as F:
        for a,b,c,d,e,f,g,h in zip(APG_Clade_list,
                     APG_Order_list,
                     APG_Family_list,
                     Kew_Family_list,
                     Genus_list,
                     Species_Epithet_list,
                     Species_Author_list,
                     Weight_list):
            F.write('{},{},{},{},{},{},{},{}\n'.format(a,b,c,d,e,f,g,h))##csvファイルに保存



with open('deepurls.csv') as fp:
    urllist = list(csv.reader(fp))
    
duetime=0
maxduetime=10
maxedduetime=0
amounturl_list=list()
resetlist

def checkers():
    global truelist
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    print("finishedurl"+str(fin))
    start=amount-fin
    if start >= 100:
        print("good")
        truelist=urllist[int(fin):int(fin+100)]
        
        file = open('finishedurl.txt', 'w')  #書き込みモードでオープン
        string = str(fin+100)
        file.write(string)

    else:
        print("less")
        truelist=urllist[int(fin):]
        
        file = open('finishedurl.txt', 'w')  #書き込みモードでオープン
        string = str(amount)
        file.write(string)

    

for cal in range(maxduetime):
    urle=open("urlnumber.txt").read()
    amounte=float(urle)
    finurle=open("finishedurl.txt").read()
    fine=float(finurle)
    print(str(fine)+"/"+str(amounte)+"is done before this process")
    if fine == amounte:
        print("fininished")
        
    else:
        checkers()
        
        for urlss in truelist:
            print(str(urlss))
            a1=((str(urlss)).replace("[","")).replace("]","")
            a2=a1.replace("'","")
            getter(a2)
            print("")
        writer()
        
            



        
        

    


