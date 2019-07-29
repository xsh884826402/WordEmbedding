import os
def load_w2c_textcn_dataset(path='./data/raw_lu_id_with_ordered_id.csv'):
    '''
    :param path:  语料的路径,
    :return: word_list_all: 二维列表
        a list if strng(word)\n
    '''
    print("Load or Download corpus Dataset :",path)

    word_list_all = []
    with open(path) as f:
        for line in f:
            #word_list 一行数据
            temp = []
            word_list = line.strip().split("|")
            temp.extend(word_list[0].strip().split())
            temp.extend(word_list[1].strip().split())
            word_list_all.append(temp)

    print(word_list_all[0])
    return word_list_all


if __name__ =="__main__":
    words = load_w2c_textcn_dataset()
    print(len(words), type(words), type(words[0]))