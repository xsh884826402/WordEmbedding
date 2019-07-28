import numpy as np
import collections
import random
import pickle
data_index = 0
with open("./data/data.txt","rb") as f:
    data = pickle.load(f)
    print(type(data),type(data[0]))
with open("./data/dict_word_index.txt",'rb') as f:
    dic = pickle.load(f)
def batch_generate(batch_size,num_skips,skip_window):
    """

    :param batch_size:
    :param num_skips:
    :param skip_window:
    :return: 返回batch 和 labels
    """
    print("IN batch_generate")
    global data_index
    batch = np.ndarray(shape=(batch_size),dtype=np.int64)
    labels = np.ndarray(shape=(batch_size,1),dtype= np.int64)

    span = 2*skip_window + 1
    buf = collections.deque(maxlen=span)
    # buf 里面添加了span个 房源id,buf中始终保持span个词
    #跳过未出现的房源id
    index = 0
    while(index<span):
        while(data[data_index] not in dic.keys()):
            data_index = (data_index + 1) % len(data)
        buf.append(data[data_index])
        index += 1
        data_index = (data_index + 1)% len(data)
    for i in range(batch_size// num_skips):
        #target label  at the center of the buffer
        target = skip_window
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0,span -1 )
            targets_to_avoid.append(target)
            batch[i*num_skips + j] =buf[skip_window]
            labels[i*num_skips +j,0] = buf[target]
        #注意跳过未出现过得房源ID
        while(data[data_index] not in dic.keys()):
            data_index = (data_index+1) % len(data)
        buf.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    return batch,labels

