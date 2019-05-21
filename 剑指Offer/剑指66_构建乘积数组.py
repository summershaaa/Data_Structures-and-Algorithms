# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:24:59 2019

@author: WinJX
"""
#剑指66：构建乘积数组


class Solution:
    def multiply(self, A):
        # write code here
        rst = [0]*len(A)
        for val in range(len(A)):
            rst[val] = A[:val]+A[val+1:]
        rst = list(map(lambda x:self.cumsum(x),rst))
        return rst
    
    def cumsum(self,n):
        ans = 1
        for i in n:
            ans *= i
        return ans
    
rst = Solution()
print(rst.multiply([1,2,3,4,5]))