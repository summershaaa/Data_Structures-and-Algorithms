# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:16:34 2019

@author: WinJX
"""
#剑指43:1到n整数中1出现的次数

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if not n:
            return 0
        count = 0
        for i in range(1,n+1):
            tmp = str(i).count('1')
            count += tmp
        return count
    
rst = Solution()
print(rst.NumberOf1Between1AndN_Solution(21345))
print(rst.NumberOf1Between1AndN_Solution(0))