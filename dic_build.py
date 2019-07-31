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
    words = data_load.load_w2c_textcn_dataset()
    # 注意这里Counter返回的类型
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()

    for word, _ in count:
        # print(dictionary)
        dictionary[word] = len(dictionary)
    # data是label
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count = unk_count + 1
        data.append(index)
    count[0][1] = unk_count

    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    with open('./data/dict_word_index.txt','wb') as f:
        pickle.dump(dictionary, f)
    with open("./data/data.txt", "wb") as f:
        pickle.dump(data, f)
    with open("./data/dict_index_word.txt","wb") as f:
        pickle.dump(reverse_dictionary, f)

if __name__ =="__main__":
    dic_build()