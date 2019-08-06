# -*- coding: utf-8 -*-
# @Time    : 2019-08-06 14:12
# @Author  : Xushenghua
# @File    : datadeal1.py
import numpy as np
import pandas as pd
from datetime import timedelta, datetime
#yesterday = datetime.today() + timedelta(-1)
todayy=datetime.today().strftime('%Y-%m-%d')
aaa=pd.read_csv(f'/data1/xushenghua/embedding/sqldata/embsql{todayy}.csv',sep='\t',error_bad_lines=False)

bbb=[tuple(x) for x in aaa.values]
record = {}
index=1
timeend=0
for userid,luid,view_time,timesec,book_luid in bbb:
    if userid not in record:
        record[userid] = []
        timetstart = timesec

        # timeend=timesec+1800
    if timesec-timetstart<=1800:
        record[userid].append(luid)
        timetstart = timesec
        # index=index+1
    else:
        record[userid].append(book_luid)
        timetstart = timesec
        record[userid].append('\n')
        record[userid].append(luid)

fw = open(f'/data1/xushenghua/embedding/traindata/traindata{todayy}.txt', 'w+')
for userid in record:
    fw.write(" ".join('%s' %id for id in (record[userid])) + "\n")
fw.close()
