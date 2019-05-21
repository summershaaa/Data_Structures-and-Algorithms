# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:03:35 2019

@author: WinJX
"""
"""
剑指64：求1+2+3+...+n
要求不能使用乘除法、for、while、if、else、switch、case等关键字
及条件判断语句（A?B:C）。
"""

class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        #return n and self.Sum_Solution(n-1)+n
        self.add(n)
        return self.sum
    
    def add(self,n):
        self.sum += n
        n -= 1
        return n>0 and self.add(n)
    
rst = Solution()
print(rst.Sum_Solution(100))