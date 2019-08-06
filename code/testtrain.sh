#!/usr/bin/env bash
#/bin/sh
#取系统时间

vDate=`date +%Y-%m-%d`
{
echo $vDate

nohup python3 /data1/embedding/code/testtrain.py > /data1/embedding/log/tarin$vDate.log 2>&1 &

}>>/data1/embedding/log/test1.log
