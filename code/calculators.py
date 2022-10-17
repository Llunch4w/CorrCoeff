# !/user/bin/env python
# _*_ coding: utf-8 _*_
'''
@Time        :   2022/10/16 11:05:43
@Author      :   LuckyQ
@Version     :   1.0
@Description :   相关系数计算器
'''
import math
from loguru import logger

class CorrelationCalculator():
    
    def calculate(self, x, y):
        assert len(x) == len(y)
        assert len(x) > 0
    

class Pearson(CorrelationCalculator):
    def calculate(self, x, y):
        try:
            super(Pearson, self).calculate(x, y)
            sigma = lambda n: len(n) * sum(map(lambda i: i**2, n)) - (sum(n) ** 2)
            logger.info(zip(x, y))
            E_XY = len(x) * sum(map(lambda a: a[0] * a[1], zip(x, y)))
            EX_EY = sum(x) * sum(y)
            result = (E_XY - EX_EY) / math.sqrt(sigma(x)*sigma(y))
            return result
        except Exception:
            logger.exception("Pearson calculate error")
            return None
    
    
class Spearman(CorrelationCalculator):
    def calculate(self, x, y):
        try:
            super(Spearman, self).calculate(x, y)
            to_index = lambda n: map(lambda val: sorted(n).index(val)+1, n)
            d = sum(map(lambda x, y: (x - y)**2, to_index(x), to_index(y)))
            n = len(x)
            res = 1.0 - 6.0 * d / float(n*(n**2 - 1.0))
            return res
        except Exception:
            logger.exception("Spearman calculate error")
            return None
    
        
class Kendall(CorrelationCalculator):
    def calculate(self, x, y):
        try:
            super(Kendall, self).calculate(x, y)
            n = len(x)
            t = 0
            for i in range(len(x)):
                for j in range(i+1):
                    s = (x[i] - x[j]) * (y[i] - y[j])
                    if s > 0:
                        t += 1
                    elif s < 0:
                        t -= 1
            res = 2 * t / float(n*(n-1))
            return res
        except Exception:
            logger.exception("Kendall calculate error")
            return None

calculators_map = {
    "pearson": Pearson(),
    "spearman": Spearman(),
    "kendall": Kendall()
}             