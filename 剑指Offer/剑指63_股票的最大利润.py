# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:30:30 2019

@author: WinJX
"""

#剑指63：股票的最大利润
class Solution:
    def MaxDiff(self,array):
        if len(array)<2:
            return 0
#        min_val = array[0]
#        max_diff = array[1] - min_val
#        for i in range(2,len(array)):
#            if array[i-1] < min_val:
#                min_val = array[i-1]
#            cur_diff = array[i] - min_val
#            if cur_diff > max_diff:
#                max_diff = cur_diff
#        return max_diff
            
        #动态规划f(n) = max(f(n-1),f(n)-min[n-1])
        min_val = array[0]
        max_diff = array[1] - min_val
        for i in range(2,len(array)):
            min_val = min(min_val,array[i-1])
            max_diff = max(max_diff,array[i]-min_val)
        return max_diff
        
    
rst = Solution()
print(rst.MaxDiff([9,11,8,5,7,12,16,14]))
print(rst.MaxDiff([7,1,5,3,6,4]))