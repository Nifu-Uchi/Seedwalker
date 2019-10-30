#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:48:46 2018

@author: hiro.t
"""


import csv
a1=list("apple","bear","car",)
a2=list("one","two","three",)
csvfile=open('test2.csv',"w+",newline='')
write=csv.writer(csvfile)
for a in a1:
    write.writerow(a,)

