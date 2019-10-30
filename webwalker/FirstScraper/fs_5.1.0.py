#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:43:12 2018

@author: hiro.t
"""

import os
filename="test"
os.makedirs(filename, exist_ok=True)

nameslist=()
weightlist=()
htmllist=()
cate="a"
with open(filename+"/"+cate+".csv",'w') as F:
        for a,b,c in zip(nameslist,weightlist,htmllist):
            F.write('{},{},{}\n'.format(a,b,c))