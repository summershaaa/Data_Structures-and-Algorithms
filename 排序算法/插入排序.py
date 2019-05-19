# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:25:50 2019

@author: WinJX
"""

#插入排序：最好情况：顺序O(n)
#稳定排序 最坏情况：逆序O(n)

class Solution:
    def Insert_Sort(self,nums):
        if len(nums) <= 1:
            return nums
        #从第二个数字到最后一个数字
        for i in range(1,len(nums)):
            #print(nums)
            #从第i个数字到第1个数字。不能到第0个，因为第0个数字没有前驱数字可比较了
            for j in range(i,0,-1):
                #如果当前数字比前驱数字小，则向前挪一位
                if nums[j-1] > nums[j]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
        return nums

nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.Insert_Sort(nums))
print(rst.Insert_Sort(nums1))
print(rst.Insert_Sort([]))
print(rst.Insert_Sort([1]))