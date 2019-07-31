import pickle
import numpy
def prac():
    with open("./data/word2vec.txt","rb") as f:
        word2vec = pickle.load(f)
        print(type(word2vec),word2vec[0],numpy.shape(word2vec))
if __name__ == "__main__":
    prac()