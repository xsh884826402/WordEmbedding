import os
def load_w2c_textcn_dataset(path='./data/raw_lu_id.csv'):
    '''
    :param path:  语料的路径,
    :return: word_list_all: a list
        a list if strng(word)\n
    '''
    print("Load or Download corpus Dataset :",path)

    #filename = 'wiki_cn_cut'
    word_list_all = []
    with open(path) as f:
        for line in f:
            #word_list 一行数据
            word_list = line.strip().split()
            for idx, word in enumerate(word_list):
                word_list_all.append(word_list[idx])
    return word_list_all


if __name__ =="__main__":
    words = load_w2c_textcn_dataset()
    print(len(words), type(words), type(words[0]))