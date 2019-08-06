# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import os
import re


today = datetime.today()
today = today.strftime('%Y-%m-%d')
print(today)


def clean_tmp():
    tmp_dir1 = '/data1/embedding/temp'
    # print(tmp_dir1)
    command1 = f'rm -rf {tmp_dir1}/*'
    os.system(command1)

    tmp_dir2 = '/data1/embedding/traindata'
    # print(tmp_dir1)
    command2 = f'rm -rf {tmp_dir2}/*'
    os.system(command2)

    tmp_dir3 = '/data1/embedding/sqldata'
    # print(tmp_dir1)
    command3 = f'rm -rf {tmp_dir3}/*'
    os.system(command3)


def clean_resultdata():

    sqlreslist = os.listdir(f'/data1/embedding/result/')
    for x in sqlreslist:
        datee=re.split("c|\.",x)[1]

        if datee not in [today]:
            print(f'删除文件：/data1/embedding/result/{x}')
            os.remove(f'/data1/embedding/result/{x}')

clean_tmp()
clean_resultdata()
