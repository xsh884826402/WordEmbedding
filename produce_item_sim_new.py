# -*- coding: utf-8 -*-

import os
import numpy as np
import operator
import sys

FILE_PATH = os.path.dirname(__file__)

def load_item_vec(input_file):
    """
    Args:
        input_file: item vec file
    Return:
        dict key:itemid value:np.array([num1, num2....])
    """
    input_file = os.path.join(FILE_PATH, input_file)

    if not os.path.exists(input_file):
        print(input_file)
        print('not os.path exist')
        return {}
    linenum = 0
    item_vec = {}
    fp = open(input_file)
    for line in fp:
        # print("line",line)
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split()
        # if len(item) <= 64:
        #     continue
        itemid = item[0]
        vector = item[1].strip().split(',')
        if itemid == "</s>":
            continue
        item_vec[itemid] = np.array([float(ele) for ele in vector])
    fp.close()
    return item_vec


def cal_item_sim(item_vec, itemid, output_file):
    """
    Args
        item_vec:item embedding vector
        itemid:fixed itemid to clac item sim
        output_file: the file to store result
    """
    output_file = os.path.join(FILE_PATH, output_file)

    if itemid not in item_vec:
        print(output_file)
        print('itemid not in')
        return
    score = {}
    topk = 10
    fix_item_vec = item_vec[itemid]
    for tmp_itemid in item_vec:
        if tmp_itemid == itemid:
            continue
        tmp_itemvec = item_vec[tmp_itemid]
        fenmu = np.linalg.norm(fix_item_vec) * np.linalg.norm(tmp_itemvec)
        if fenmu == 0:
            score[tmp_itemid] = 0
        else:
            score[tmp_itemid] =  round(np.dot(fix_item_vec, tmp_itemvec)/fenmu, 3)
    fw = open(output_file, "a+")
    out_str = itemid + "\t"
    tmp_list = []
    for zuhe in sorted(score.items(), key = operator.itemgetter(1), reverse = True)[:topk]:
        tmp_list.append(zuhe[0] + "_" + str(zuhe[1]))
    out_str += ";".join(tmp_list)
    fw.write(out_str + "\n")
    fw.close()
    print('done')


def run_main(input_file, output_file):
    input_file = os.path.join(FILE_PATH, input_file)
    output_file = os.path.join(FILE_PATH, output_file)

    with open('./data/luid.txt', 'r') as file:
        itemlist = file.readlines()
    itemid = [x.strip() for x in itemlist]
    item_vec = load_item_vec(input_file)
    print('keys',item_vec.keys())
    item_vec_keys = item_vec.keys()
    # for key in item_vec_keys:
    #     print("length",len(item_vec_keys),"key",key)
    for i in itemid:
        print(i,type(i))
        cal_item_sim(item_vec, str(i), output_file)


if __name__ == "__main__":
        run_main("./data/item_vec_new.txt", "./data/sim_result_new.txt")