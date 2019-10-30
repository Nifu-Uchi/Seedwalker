#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:13:07 2018

@author: hiro.t
"""
import csv

with open('species.csv') as cs:
    splist = list(csv.reader(cs))

with open('genus.csv') as cs:
    genlist = list(csv.reader(cs))
gen_splist=list()
numm=len(genlist)
print(numm)
    
