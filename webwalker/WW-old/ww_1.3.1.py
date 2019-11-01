#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:56:02 2018

@author: hiro.t
"""
#初期設定
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep
counter=0
"""メール送信用コンソール"""
"""初期化"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
charset       = "iso-2022-jp"
myMailaddress = "hirex0609@gmail.com" # 自分のGmailアドレス
password      = "yukumomura1996"                      # Gmailアカウントのパスワード
toMailaddress = "hirex0609@gmail.com"     # 送信相手のメールアドレス
Ltit=""
Lmain=""
title=""
mainbody=""
"""保存先ファイルの作成"""
import os
filename="seedweightlist"
os.makedirs(filename, exist_ok=True)


"""関数の定義"""
def Mailer(Ltit,Lmain):
    title=Ltit
    mainbody=Lmain
    msg = MIMEText(mainbody.encode(charset), 'plain', charset)     # メール本文
    msg["subject"] = Header(title.encode(charset), charset) 
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)    # Gmailはポート番号587のTLSをサポートしていない！よくわからなければスルーしてね。
    smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465) # Gmailでのメール送信は「smtplib.SMTP_SSL」を用いてポート番号465を使用すること。
    smtp_obj.ehlo()                                    # ehlo()でSMTPサーバーに挨拶しておきましょう。挨拶しておかないとログインできません！
    smtp_obj.login(myMailaddress, password)            # ログイン
    smtp_obj.sendmail(myMailaddress, toMailaddress, msg.as_string()) # メール送信
    smtp_obj.quit()                                    # ログアウト
    print("mail send to "+toMailaddress)                                   #送信完了のメッセージ
    ##各関数の初期化
    title=""
    mainbody=""
    Ltit=""
    Lmain=""
"""関数の定義ここまで"""    


"""任意のタイトルとかをきめるやつ"""

##Ltit、Lmain　に送りたい件名と本文を入れる

"""メール送信用コンソールここまで"""

"""処理する分類名を一覧にする関数"""
catslist=list()
def catgetter(urls):
    a1=(((urls.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")).replace("&Order=","-"))
    a2=a1.replace("+","")
    a3=a2.replace("\n","-")
    catslist.append(a3)
    
"""関数listeｒの定義"""    
##各URLに対して名前と重さidを取得し、リストにする    
def lister(urls):
    int(counter)
    print("Count."+str(counter))
    print("accessing  "+urls)
    html=urlopen(urls)
    bsObj=BeautifulSoup(html,"lxml")
    print("accessed!")
    sleep(0.5)
    linkslist=list()
    nameslist=list()
    weightlist=list()
    htmllist=list()
    nameslist.append("name")
    htmllist.append("URL")
    cates=(((urls.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")).replace("&Order=","-"))
    catess=cates.replace("+","")
    cate=catess.replace("\n","-")
    print("========="+cate+"list START!")
    sleep(1)



    ##idを取得
    print("==get id_start==")
    sleep(1)
    for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
        if 'href' in basedlink.attrs:
            linkslist.append(basedlink.attrs['href'])

    for linkid in linkslist:    
        print("http://data.kew.org/sid/"+linkid)
        htmllist.append("http://data.kew.org/sid/"+linkid)
        
   
    print("get"+str(len(htmllist))+"urls")
    print("==get id_end==" )
    
    ##名前を取得
    print("==get name_start==" )
    sleep(1)
    
    for ids in linkslist:
        names = bsObj.findAll("a",{"href":ids})
        for name in names:
            nameslist.append(name.get_text())
            print(name.get_text())
           
    print("get"+str(len(nameslist)))
    print("==get name_end==" )   
     
    ##重さを取得
    print("==get weight_start==" ) 
    sleep(1)
    weights=bsObj.findAll("span", {"style":"COLOR: navy"})
    for weight in weights:
        weightlist.append((weight.get_text()).replace("g",""))##gを取り除いてリスト化
        print((weight.get_text()).replace("g",""))
        
    print("==get weight_end==" )
    print("get"+str(len(weightlist)))
    ##一覧を保存
    print("==write csv==" ) 
    sleep(1)
    with open(filename+"/"+cate+".csv",'w') as F:
        for a,b,c in zip(nameslist,weightlist,htmllist):
            F.write('{},{},{}\n'.format(a,b,c))

    print("========="+cate+"list DONE!")
    Ltit=(cate+"list DONE!")
    Lmain=("get"+str(len(weightlist)))
    Mailer(Ltit,Lmain)
    sleep(1)
"""関数ここまで"""
   
##メイン  
urllist=list(open("urls.txt"))
for geturl in urllist:
    print(geturl)
urlnumber=str(len(urllist))+"URL is here"
print(urlnumber)
sleep(1)
print("Process is starting..........")

 ##処理するサイトの分類名を一覧にしてメールで送信
for cat in urllist:
    catgetter(cat)
Ltit=("Process Starting "+urlnumber+"sites")
Lmain=("get"+urlnumber+"and all process start"+
       str(catslist))
Mailer(Ltit,Lmain)

##URLをListerで処理する
for sites in urllist:
    counter=counter+1
    lister(sites)
    print(sites+"is done")

##終了通知  
print("done")
Ltit=("All process is DONE")
Lmain=("get"+urlnumber+"and all process DONE")
Mailer(Ltit,Lmain)