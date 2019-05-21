# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:58:25 2019

@author: WinJX
"""

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if all([x==0 for x in numbers]): 
            return ""
        nums = [str(x) for x in numbers]
        #相当于每一轮外循环把当前最小的值放前面
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if self.orde(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)
    
    def orde(self,x1, x2):
            return x1+x2 > x2+x1
rst = Solution()
numbers = [3,32,321]
print(rst.PrintMinNumber(numbers))
print(rst.PrintMinNumber([1,2,3,4,5]))
print(rst.PrintMinNumber([]))