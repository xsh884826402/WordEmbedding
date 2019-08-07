import pickle
import numpy
if __name__ =="__main__":
    with open("./data/dict_word_index.txt",'rb') as f:
        dic = pickle.load(f)
    with open("./data/word2vec.txt", 'rb') as f:
        word2vec = pickle.load(f)
    with open("./data/item_vec_new.txt","wb") as f:
        for key in dic.keys():
            vec = word2vec[dic[key]].tolist()
            vec = [str(i) for i in vec]
            f.write(str(key)+' '+",".join(vec)+'\n')