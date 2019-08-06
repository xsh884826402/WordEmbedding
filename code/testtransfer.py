# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from datetime import timedelta, datetime
todayy=datetime.today().strftime('%Y-%m-%d')
def produce_transfer_data(input_file, out_file):
    fp = open(input_file)
    result = list()
    for line in fp.readlines():
        line = ",".join(line.split())[:-1]
        line = line.replace(',',' ',1)
        result.append(line+'\n')
        fp.close
    fw = open(out_file, 'w+')
    fw.write(''.join(result[2:]))
    fw.close()

if __name__ == "__main__":
    produce_transfer_data(f'/data1/embedding/temp/item_vectest{todayy}.txt', f'/data1/embedding/result/item_vectest{todayy}.txt')
