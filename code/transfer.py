import numpy as np
import pandas as pd

from datetime import timedelta, datetime
todayy=datetime.today().strftime('%Y-%m-%d')

def ave_wordvec(input_file,out_file):
    print('start')
    f = open(input_file)
    lines = f.readlines()
    lines = lines[2:]
    result = []
    for line in lines:
        result.append(line.split())

    sorted_result = sorted(result,key= lambda line:line[0])
    final_result = []
    le = len(sorted_result)
    i = 0
    while(i<le):
        if i+1<le and sorted_result[i][0]+'.0' == sorted_result[i+1][0]:
            lu_id = sorted_result[i][0]
            temp_line = []
            for index in range(len(sorted_result[i])):
                temp_line.append((float(sorted_result[i][index]) + float(sorted_result[i + 1][index])) / 2)
            temp_line[0] = lu_id
            final_result.append(str(temp_line[0]) + ' ' + ",".join([str(x) for x in temp_line[1:]]) + '\n')
            i+=2
        else:
            final_result.append(str(sorted_result[i][0]) + ' ' + ",".join([str(x) for x in sorted_result[i][1:]]) + '\n')
            i+=1
    f.close()
    fw = open(out_file,'w+')
    fw.write("".join(final_result))
    fw.close()
    print('finish')



if __name__ == "__main__":
    ave_wordvec(f'/data1/embedding/temp/item_vec{todayy}.txt', f'/data1/embedding/result/item_vec{todayy}.txt')
