#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 00:47:47 2018

@author: hiro.t
"""
from time import sleep
import time
import threading
import time
import concurrent.futures

def checkers1():
    check1=open("stait.txt").read()
    checker1=float(check1)
    print(checker1)
    if checker1 == 0:
        print("ok1")
        checker1=checker1+1
        (open('stait.txt', 'w')).write(str(checker1))
        sleep(1)
        checkers1()

    else:
        print("bad1")
        sleep(2)
        checkers1()
        
def checkers2():
    check2=open("stait.txt").read()
    checker2=float(check2)
    print(checker2)
    if checker2 == 1:
        print("ok2")
        checker2=checker2-1
        (open('staittxt', 'w')).write(str(checker2))
        time.sleep(1)
        checkers2()

    else:
        print("bad2")
        ti,sleep(2)
        checker2()
    
    
func1=checkers1()
func2=checkers2()

if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor.submit(func1)
    executor.submit(func2)


