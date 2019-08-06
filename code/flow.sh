#!/usr/bin/env bash
#/bin/sh
#取系统时间

vDate=`date +%Y-%m-%d`
yester=`date -d"-1 day" +%Y-%m-%d`
{
echo $vDate

/usr/bin/hive -f /data1/embedding/code/embedding.sql  > /data1/embedding/sqldata/embsql$vDate.csv
if [ $? -eq 0 ]; then
		echo "====sql数据下载成功===="

else
		echo "====sql数据下载失败===="
fi


sqllenth=`cat /data1/embedding/sqldata/embsql$vDate.csv | wc -l`

echo $sqllenth

if [ $sqllenth > 15000000 ]; then
        echo "====sql数据正常===="
else
		echo "====sql数据过小===="
fi

python3 /data1/embedding/code/traindatadeal.py 

if [ $? -eq 0 ]; then
		echo "====训练数据处理成功===="

else
		echo "====训练数据处理失败===="
fi


train_file="/data1/embedding/traindata/traindata${vDate}.txt"
item_vec_file="/data1/embedding/temp/item_vec${vDate}.txt"

/data1/embedding/code/word2vec -train $train_file -output $item_vec_file -size 64 -window 5 -sample 1e-3 -negative 5 -hs 0 -binary 0 -cbow 0 -iter 50


if [ $? -eq 0 ]; then
		echo "====模型训练完成===="

else
		echo "====模型训练失败===="
fi



python3 /data1/embedding/code/transfer.py

if [ $? -eq 0 ]; then
		echo "====落表数据处理成功===="

else
		echo "====落表数据处理失败===="
fi


/usr/bin/hive -e "load data local inpath '/data1/embedding/result/item_vec$vDate.txt' overwrite into table algorithm.mds_lu_embedding_da partition(dt='${yester}');"

if [ $? -eq 0 ]; then
		echo "====落表成功===="

else
		echo "====落表失败===="
		exit 1
fi


python3 /data1/embedding/code/Clearup.py
}>>/data1/embedding/log/$vDate.log
