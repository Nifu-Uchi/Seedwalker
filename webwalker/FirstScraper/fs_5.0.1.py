#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:08:22 2018

@author: hiro.t
"""
"""
http://freemanplaying.com/2017/11/30/python%E3%81%A7gmail%E3%81%8B%E3%82%89%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%92%E9%80%81%E4%BF%A1%E3%81%97%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86%EF%BC%81/\
"""

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
Ltit="test"
Lmain="test"
Mailer(Ltit,Lmain)  #送る
"""メール送信用コンソールここまで"""
