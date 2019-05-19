# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:49:32 2019

@author: WinJX
"""

#希尔排序

class Solution:
    def Shell_Sort(self,nums):
        if len(nums) <= 1:
            return nums
        gap = len(nums)//2
        #间隔不断缩小到1
        while gap > 0:
            #从gap到最后一个元素不断做插入排序
            for i in range(gap,len(nums)):
                #当满足前gap位的数字比当前数字大时，交换位置，并把下标向前挪gap位
                while i-gap >= 0 and nums[i] < nums[i-gap]:
                    nums[i],nums[i-gap] = nums[i-gap],nums[i]
                    i -= gap
            #一轮比较后，缩小间隔直到1
            gap = gap//2
        return nums
    
nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.Shell_Sort(nums))
print(rst.Shell_Sort(nums1))
print(rst.Shell_Sort([]))
print(rst.Shell_Sort([1]))