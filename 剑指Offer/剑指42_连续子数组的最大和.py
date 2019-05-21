# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:01:25 2019

@author: WinJX
"""
#剑指42：连续子数组的最大和
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        rst = array[0]
        cur_sum = 0
#        for val in array:
#            if cur_sum <= 0:
#                cur_sum = val
#            else:
#                cur_sum += val
#            if cur_sum > rst:
#                rst = cur_sum
#        return rst
        #动态规划 ： f(i) = max(data[i],data[i]+f(n-1))
        for val in array:
            cur_sum = max(val,cur_sum + val)
            rst = max(cur_sum,rst)
        return rst

rst = Solution()
array = [1,-2,3,10,-4,7,2,-5]
print(rst.FindGreatestSumOfSubArray(array))
print(rst.FindGreatestSumOfSubArray([]))