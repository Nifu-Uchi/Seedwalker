#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:16:52 2018

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

def resetlist():
    APG_Clade_list=list("APG_Clade")
    APG_Order_list=list("APG_Clade")
    APG_Family_list=list("APG_Clade")
    Kew_Family_list=list("APG_Clade")
    Genus_list=list("APG_Clade")
    Species_Epithet_list=list("APG_Clade")
    Species_Author_list=list("APG_Clade")
    
targetlist=list()    
targetlist.append("APG Clade: ")    
targetlist.append("APG Order: ")    
targetlist.append("APG Family: ")    
targetlist.append("Kew Family: ")    
targetlist.append("Genus: ")    
targetlist.append("Species Epithet: ")    
targetlist.append("Species Author: ")
    
collectionlist=list() 
collectionlist.append("APG_Clade_list")
collectionlist.append("APG_Order_list")
collectionlist.append("APG_Family_list")
collectionlist.append("Kew_Family_list")
collectionlist.append("Genus_list")
collectionlist.append("Species_Epithet_list")
collectionlist.append("pecies_Author_list")

        
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


    
        


"""メインフレーム"""
URLlist=list(open("deepurls.txt"))
resetlist()
counter=0
for (URL) in (URLlist):
    collector(URL)
    counter=counter+1
    print(str(counter))
    
with open(str(counter)+"splist.csv",'w') as F:
    for a,b,c,d,e,f,g in zip(APG_Clade_list,
                     APG_Order_list,
                     APG_Family_list,
                     Kew_Family_list,
                     Genus_list,
                     Species_Epithet_list,
                     Species_Author_list):
        F.write('{},{},{},{},{},{},{}\n'.format(a,b,c,d,e,f,g))##csvファイルに保存
