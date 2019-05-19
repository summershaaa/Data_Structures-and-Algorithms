# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:20:33 2019

@author: WinJX
"""

class Solution:
    def Select_Sort(self,nums):
        if len(nums) <= 1:
            return nums
        for i in range(0,len(nums)):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums
    
nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.Select_Sort(nums))
print(rst.Select_Sort(nums1))
print(rst.Select_Sort([]))
print(rst.Select_Sort([1]))