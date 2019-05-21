# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:54:58 2019

@author: WinJX
"""
#剑指59：队列的最大值
class Solution:
    #题目1：滑动窗口的最大值
    def maxInWindows(self, num, size):
        # write code here
        if not num or len(num)<size or size <=0:
            return []
        rst = []
        for start in range(len(num)-size+1):
            rst.append(max(num[start:start+size]))
        return rst
    
    
    
rst = Solution()
print(rst.maxInWindows([2,3,4,2,6,2,5,1],4))