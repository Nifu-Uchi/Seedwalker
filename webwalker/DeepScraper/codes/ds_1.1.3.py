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
counter=0
def resetlist():
    APG_Clade_list=list("APG_Clade")
    APG_Order_list=list("APG_Clade")
    APG_Family_list=list("APG_Clade")
    Kew_Family_list=list("APG_Clade")
    Genus_list=list("APG_Clade")
    Species_Epithet_list=list("APG_Clade")
    Species_Author_list=list("APG_Clade")
tar=""
def collector(URL):
    
    html=urlopen(URL)
    bsObj=BeautifulSoup(html,"lxml")
    tex=bsObj.get_text()
    

    tar="APG Clade: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    APG_Clade_list.append(coll)
    print(coll)
    
    tar="APG Order: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    APG_Order_list.append(coll)
    print(coll) 
    
    tar="APG Family: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    APG_Family_list.append(coll)
    print(coll) 
    
    tar="Kew Family: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    Kew_Family_list.append(coll)
    print(coll)
    
    tar="Genus: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    Genus_list.append(coll)
    print(coll) 
    
    tar="Species Epithet: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    Species_Epithet_list.append(coll)
    print(coll) 
    
    tar="Species Author: "
    coll=(re.search(tar+"(.*)",tex).group(1)).replace(",","★")
    Species_Author_list.append(coll)
    print(coll) 


    
        


def getter(urlname):
    global counter
    print("gettr")
    collector(urlname)
    counter=counter+1
    print(str(counter))
    
def writer():    
    with open(str(counter)+"splist.csv",'a') as F:
        for a,b,c,d,e,f,g in zip(APG_Clade_list,
                     APG_Order_list,
                     APG_Family_list,
                     Kew_Family_list,
                     Genus_list,
                     Species_Epithet_list,
                     Species_Author_list):
            F.write('{},{},{},{},{},{},{}\n'.format(a,b,c,d,e,f,g))##csvファイルに保存



with open('deepurls.csv') as fp:
    urllist = list(csv.reader(fp))
    
duetime=0
maxduetime=30
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
    if fine == amounte:
        print("fininished")
        
    else:
        checkers()
        print(truelist)
        for urlss in truelist:
            print(str(urlss))
            sleep(3)
            a1=((str(urlss)).replace("[","")).replace("]","")
            a2=a1.replace("'","")
            getter(a2) 
            



        
        

    


