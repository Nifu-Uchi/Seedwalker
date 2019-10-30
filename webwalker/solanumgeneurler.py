#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:02:05 2018

@author: hiro.t
"""


import csv
import re
from time import sleep



epitlist=list(open("dates/COMP_epit.txt"))
COMPlen=len(epitlist)
URLpA="https://scholar.google.co.jp/scholar?as_vis=1&q="
URLpB="+self+compatibility&btnG="
COMPurl=list()

for numb in range(1,COMPlen):
    COMPURL=""

    gen=re.sub('\n',"",genelist[numb])
    epit=re.sub('\n',"",epitlist[numb])
    COMPURL=URLpA+gen+"+"+'"'+epit+'"'+URLpB
    print(COMPURL)
    COMPurl.append(COMPURL)

with open("dates/CPMPurl.txt", mode='w') as f:
    f.writelines('\n'.join(COMPurl))
    
    
"""    
    gen=genelist[numb].replace('\n',"")
    epit=epitlist[numb].replace('\n',"")
"""