#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:26:32 2018

@author: hiro.t
"""
"""初期設定"""
import csv
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
Weight_list=list()
amounturl_list=list()
counter=0
duetime=0
maxduetime=10#100×maxduetime実行する。
maxedduetime=0
tar="" #collectorで使う変数

"""各種関数の定義""" 
def nocheck(col0):#collectorが取り出した各データがNullかどうかを判定し、Nullならデータ値を”NONE”にして返す。
    global coll
    if col0 != None:
        coll=(col0.group(1)).replace(",","★")#文字列から,を取り除く。
    else:

        coll="NONE"



def collector(URL):#実際にデータを集める。nocheckを呼び出して、データがnullの場合の処理もさせる。
    html=urlopen(URL)
    bsObj=BeautifulSoup(html,"lxml")
    tex=bsObj.get_text()
    
    

    tar="APG Clade: "
    col0=re.search(tar+"(.*)",tex)
    nocheck(col0)#nocheckでデータがNull稼働かどうかを判定させる。
    APG_Clade_list.append(coll)#リストに値を追加する。
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
    

def getter(urlname):#collectorにURLを1つ渡して呼び出し、データを集める。
    global counter
    counter=counter+1
    print("--URL"+str(counter)+"count---")
    collector(urlname)
    print("----")
    
    
def writer():#collecotorがリストにしたデータをcsvファイルに保存する。  
    with open("splist.csv",'a') as F:
        for a,b,c,d,e,f,g,h in zip(APG_Clade_list,
                     APG_Order_list,
                     APG_Family_list,
                     Kew_Family_list,
                     Genus_list,
                     Species_Epithet_list,
                     Species_Author_list,
                     Weight_list):
            F.write('{},{},{},{},{},{},{},{}\n'.format(a,b,c,d,e,f,g,h))

def checkers():#Ⅰセットで処理する回数を決定する。残りURL数を確認し、100個以上かどうかで処理するファイルを決定する
    global truelist
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    print("finishedurl"+str(int(fin-1))+"/"+str(int(amounte)))
    start=amount-fin
    if start >= 100:
        print("good")
        truelist=urllist[int(fin):int(fin+100)]
        
    else:
        print("less")
        truelist=urllist[int(fin):]#100未満の場合は残り全てを処理させる。

        
def countman():#checkersの姉妹関数。同じ仕組みで残り数を判定し、完了したURL数をtxtファイルに保存する。
    global truelist
    url=open("urlnumber.txt").read()
    amount=float(url)
    finurl=open("finishedurl.txt").read()
    fin=float(finurl)
    start=amount-fin
    if start >= 100:
        print("go to next 100")
        file = open('finishedurl.txt', 'w')
        string = str(fin+100)
        file.write(string)

    else:
        print("less")
        file = open('finishedurl.txt', 'w')
        string = str(amount)
        file.write(string)

"""メインフレーム"""

with open('deepurls.csv') as cs:
    urllist = list(csv.reader(cs))
       

for cal in range(maxduetime):
    urle=open("urlnumber.txt").read()
    amounte=float(urle)
    finurle=open("finishedurl.txt").read()
    fine=float(finurle)
    print(str(int(fine-1))+"/"+str(int(amounte))+" is done before this process")
    if fine == amounte:
        print("All URL is DONE")
        
    else:
        checkers()
        
        for urlss in truelist:
            print(str(urlss))
            a1=((str(urlss)).replace("[","")).replace("]","")
            a2=a1.replace("'","")
            getter(a2)
            print("")
        writer()
        countman()



        
        

    


