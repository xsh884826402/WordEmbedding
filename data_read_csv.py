import csv
def prepare_raw_data(input,output):
    length = 3000
    count = 0
    csv_reader = open(input, 'r', encoding='utf-8')
    with open(output,"w") as f:
        # writer = csv.writer(f)
        for line in csv_reader:
            line = line.strip().split(',')
            line = [s for s in line if s!="" ]
            # print(count,line,type(line),type(line[-1]))
            if count >= length:
                break
            else:
                if len(line)>=5:
                    f.write(" ".join(line)+'\n')
                    count += 1

    return "Succeed"

if __name__ == "__main__":
    prepare_raw_data(input="./user_click_session.csv",output='./raw_lu_id.csv')
