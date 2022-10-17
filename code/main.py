# !/user/bin/env python
# _*_ coding: utf-8 _*_
'''
@Time        :   2022/10/16 22:51:53
@Author      :   LuckyQ
@Version     :   1.0
@Description :   main.py
'''
import argparse
from loguru import logger
from calculators import calculators_map

def load_data(file_path):
    X, Y = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            x, y = line.strip().split()
            X.append(float(x))
            Y.append(float(y))
    return X, Y

def load_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--calculator", type=str, default="spearman", help="the method to calculate correlation coeffcient")
    parser.add_argument("--dataset", type=str, default="./data/test.txt", help="the file path of data")
    parser.add_argument("--log_dir", type=str, default="./result", help="dir path to store log.")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = load_config()
    # logger.add(args.log_dir + "/" +"{time}.log")
    logger.add(args.log_dir + "/log.log", backtrace=True, diagnose=True)
    message = '\n'.join([f'{k:<20}:{v}' for k,v in vars(args).items()])
    logger.info(f"Configuration:\n{message}")
    
    logger.info(f"Loading data from {args.dataset}....")
    X, Y = load_data(file_path=args.dataset)
    logger.info("Loading Success!")
    logger.info(f"X = {X}\nY={Y}")
    
    calculator_name = args.calculator
    if calculator_name in calculators_map:
        calculator = calculators_map[calculator_name]
        res = calculator.calculate(X, Y)
        logger.info(f"The correlation coeffcient of {calculator_name} is {res}")