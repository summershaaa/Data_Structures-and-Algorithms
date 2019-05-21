# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:50:52 2019

@author: WinJX
"""
#剑指41：数据流中的中位数

import random
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self):
        # write code here
        if not self.data:
            return 
        length = len(self.data)
        if length&1:
            return self.data[length//2]
        return (self.data[length//2]+self.data[length//2-1])/2.0
    
rst = Solution()
#for i in random.sample(range(100),20):
#    rst.Insert(i)
rst.data = random.sample(range(100),20)
print(rst.data)
print(rst.GetMedian())