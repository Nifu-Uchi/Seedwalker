#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:56:02 2018

@author: hiro.t
"""

"""動作　要求ファイル

pyファイル直下に処理するURLを記入した、「urls.txt」を要求し
csvファイル保存用として[seedweightlist]を作製する。



対象URLからBeautifulSoupを用いて「名前　重さ　詳細ページへのリンク」の一覧を取得し、
「APGクレードーOrder.csv」の名前で保存する。
例：「EUASTERIDSⅡ」クレードの「Dipsacales」の場合
「EUASTERIDSⅡ-Dipsacales--.csv」が作製される。
(http://data.kew.org/sid/SidServlet?Clade=EUROSIDS+II&Order=Dipsacales&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on）
各処理の開始、終了時にメールにて通知を行う。
説明ここまで
以下スクリプト
"""

"""各種パッケージの導入"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from time import sleep
  

"""保存先ファイルの作成"""
import os
filename="seedweightlist" #csvファイルの保存先を指定
os.makedirs(filename, exist_ok=True)

counter=0 #現在何個目のURLを処理しているかを表示する変数

"""メール送信の初期設定"""

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



"""メール送信用関数の定義"""
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
"""メール送信用関数の定義ここまで"""    


"""任意のタイトルとかをきめるやつ"""

##Ltit、Lmain　に送りたい件名と本文を入れる

"""メール送信用コンソールここまで"""

"""処理する分類名（EUASTERIDSIとか）を一覧にする関数"""
catslist=list()
def catgetter(urls):
    a1=(((urls.replace("http://data.kew.org/sid/SidServlet?Clade=","")).replace("&Family=&APG=off&Genus=&Species=&StorBehav=0&WtFlag=on","")).replace("&Order=","-"))
    a2=a1.replace("+","")
    a3=a2.replace("\n","-") ###a1~a3でURLからAPG分類名とOrderを抽出し「APG-Order--」で返す
    catslist.append(a3)
    
"""関数listeｒ（コアプロセス）の定義"""    
##各URLに対して名前と重さidを取得し、リストにする    
def lister(urls):
    html=urlopen(urls)
    bsObj=BeautifulSoup(html,"lxml")
    linkslist=list("l")
    for basedlink in bsObj.findAll("a",href=re.compile("^(SidServlet?)")):
        if 'href' in basedlink.attrs:
            print(basedlink.attrs['href'])
            urlid=basedlink.attrs['href']
            url="http://data.kew.org/sid/"+urlid
        
            linkslist.append(url)
            print(linkslist)
    
    listnum=len(linkslist)
    print(str(listnum))
    file = open('urlnumber.txt', 'w')
    file.write(listnum)
    with open('deepurls.csv','w') as F:
        for a in zip(linkslist):
            F.write('{}\n'.format(a))
    file = open('finishedurl.txt', 'w')
    file.write("1")

"""関数ここまで"""
   
##メイン  
urllist=list(open("urls.txt"))
for geturl in urllist:
    print(geturl)
urlnumber=str(len(urllist))
print(urlnumber+"URL is here")
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
Ltit=("Process Finished "+urlnumber+"sites")
Lmain=("get"+urlnumber+"and all process start"+
       str(catslist))
Mailer(Ltit,Lmain)