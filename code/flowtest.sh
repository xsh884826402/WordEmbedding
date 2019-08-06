#!/usr/bin/env bash
#/bin/sh
#取系统时间

vDate=`date +%Y-%m-%d`
yester=`date -d"-1 day" +%Y-%m-%d`
echo $vDate

python3 /data1/embedding/code/testtrain.py 

if [ $? -eq 0 ]; then
		echo "====训练数据处理成功===="

else
		echo "====训练数据处理失败===="
fi


train_file="/data1/embedding/traindata/traindatatest${vDate}.txt"
item_vec_file="/data1/embedding/temp/item_vectest${vDate}.txt"

/data1/embedding/code/word2vec -train $train_file -output $item_vec_file -size 64 -window 5 -sample 1e-3 -negative 5 -hs 0 -binary 0 -cbow 0 -iter 50


if [ $? -eq 0 ]; then
		echo "====模型训练完成===="

else
		echo "====模型训练失败===="
fi



python3 /data1/embedding/code/testtransfer.py

if [ $? -eq 0 ]; then
		echo "====落表数据处理成功===="

else
		echo "====落表数据处理失败===="
fi


