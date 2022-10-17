#!/bin/sh

ROOT_PATH=`pwd`
DATA_PATH=${ROOT_PATH}/data
RES_PATH=${ROOT_PATH}/result
CODE_PATH=${ROOT_PATH}/code

echo "ROOT_PATH: ${ROOT_PATH}"
echo "DATA_PATH: ${DATA_PATH}"
echo "RES_PATH: ${RES_PATH}"

cd ${CODE_PATH}
python main.py \
    --calculator="kendall" \
    --dataset="${DATA_PATH}/test.txt" \
    --log_dir="${RES_PATH}"