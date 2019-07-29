import collections
import data_load
import pickle
def dic_build():
    '''
    构建词典，和按顺序的全部语料。用pickle存储
    :return:
    '''
    vocabulary_size = 200000
    count = [['unk',-1]]
    words_2D_list = data_load.load_w2c_textcn_dataset()
    words = []
    for words_1D_list in words_2D_list:
        words.extend(words_1D_list)
    # 注意这里Counter返回的类型
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()

    for word, _ in count:
        print(dictionary)
        dictionary[word] = len(dictionary)
    # data是一维列表，将房源映射到index
    data = list()
    #data_index 表明一个词在列表中的位置
    data_index = 0
    #二维列表[[book_id,min_index,end_index],...]
    bookid_range = []
    unk_count = 0
    for words_1D_list in words_2D_list:
        data_temp,bookid = words_1D_list[0:-1],words_1D_list[-1]
        min_range = data_index
        for word in data_temp:
            if word in dictionary:
                index = dictionary[word]
            else:
                index = 0
                unk_count = unk_count + 1
            data.append(index)
            data_index += 1
        #book_id range[:dataindex)
        max_range = data_index
        temp_bookid_range = [bookid,min_range,max_range]
        bookid_range.append(temp_bookid_range)

    '''for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count = unk_count + 1
        data.append(index)
    '''
    count[0][1] = unk_count

    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    with open('./data/dict_word_index.txt','wb') as f:
        pickle.dump(dictionary,f)
    with open("./data/data.txt","wb") as f:
        pickle.dump(data,f)
    with open("./data/bookid_range.txt","wb") as f:
        pickle.dump(bookid_range,f)
    print("Succeed")
if __name__ =="__main__":
    dic_build()