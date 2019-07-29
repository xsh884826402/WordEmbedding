import pickle
with open("./data/data.txt","rb") as f:
    data = pickle.load(f)
    print(data[125:128])