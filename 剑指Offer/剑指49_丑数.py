# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:53:27 2019

@author: WinJX
"""
#剑指49：丑数

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        rst = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for idx in range(index-1):
            rst.append(min(rst[idx2]*2,rst[idx3]*3,rst[idx5]*5))
            if rst[-1] == rst[idx2]*2:
                idx2 += 1
            if rst[-1] == rst[idx3]*3:
                idx3 += 1
            if rst[-1] == rst[idx5]*5:
                idx5 += 1
        return rst[-1]
        
        
        
#        if index <= 0:
#            return 0
#        num = 1
#        count = 1
#        while count < index:
#            num += 1
#            if self.ugly(num):
#                count += 1
#        return num
#    
#    def ugly(self,num):
#        while num%2 == 0:
#            num /= 2
#        while num%3 == 0:
#            num /= 3
#        while num%5 == 0:
#            num /= 5
#        return True if num==1 else False
    
rst = Solution()
print(rst.GetUglyNumber_Solution(0))
print(rst.GetUglyNumber_Solution(1))
print(rst.GetUglyNumber_Solution(2))
print(rst.GetUglyNumber_Solution(3))
print(rst.GetUglyNumber_Solution(4))
print(rst.GetUglyNumber_Solution(5))
print(rst.GetUglyNumber_Solution(6))
print(rst.GetUglyNumber_Solution(1500))