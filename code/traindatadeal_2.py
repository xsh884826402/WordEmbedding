# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 14:12
# @Author  : xushenghua
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
for userid,luid,view_time,timesec,view_date in bbb:
    if userid not in record:
        record[userid] = [userid,view_date]
        timetstart = timesec

        # timeend=timesec+1800
    if timesec-timetstart<=1800:
        record[userid].append(luid)
        timetstart = timesec
        # index=index+1
    else:
        timetstart = timesec
        record[userid].append('\n')
        record[userid].append(userid)
        record[userid].append(view_date)
        record[userid].append(luid)

fw = open(f'/data1/xushenghua/embedding/traindata/traindata{todayy}.txt', 'w+')
for userid in record:
    index = 0
    while index<len(record[userid]):
        userid_str = record[userid][index]
        view_date_str = record[userid][index+1]
        index += 2
        luid_list = []
        while record[userid][index] != '\n':
            luid_list.append(record[userid][index])
            index +=1
        luid_str = (",".join([str(i) for i in luid_list]))
        fw.write(userid_str +' '+view_date_str+' '+luid_str+'\n')
        index += 1
fw.close()
