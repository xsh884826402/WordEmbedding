import csv
def prepare_raw_data(input,output,length=3000):
    count = 0
    csv_reader = open(input, 'r', encoding='utf-8')
    with open(output,"w") as f:
        # writer = csv.writer(f)
        for line in csv_reader:
            line = line.strip().split('\t')
            temp_line = line[1].split(',')
            temp_line.extend(line[2])
            if len(temp_line)>=5:
                #这里待修改
                f.write(" ".join(temp_line[:-1])+' | ' + temp_line[-1] + '\n')
            # print(count,line,type(line),type(line[-1]))
            # if count >= length:
            #     break
            # else:
            #     if len(line)>=5:
            #         f.write(" ".join(line)+' | '+line[0]+'\n')
            #         count += 1

    print( "Succeed")

if __name__ == "__main__":
    prepare_raw_data(input="/data1/xushenghua/embedding/sqldata/embsql2019-08-07temp.csv",output='./data/raw_lu_id_with_bookid.csv',length=3000)
