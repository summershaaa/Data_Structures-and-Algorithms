# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:05:14 2019

@author: WinJX
"""
#冒泡排序，最好情况：顺序O(n)
#         最坏情况：逆序O(n^2)
#稳定排序


class Solution:
    #每轮把最小的放在最前
    def bubble_sort1(self,nums):
        if len(nums) <= 1:
            return nums
        
        for i in range(0,len(nums)):
            flag = 0
            for j in range(i,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                    flag = 1
            if not flag:
                break
        return nums
    
    #每轮把最大的放在最后
    def bubble_sort2(self,nums):
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)-1,0,-1):
            flag = 0
            for j in range(0,i):
                if nums[j] > nums[i]:
                    nums[j],nums[i] = nums[i],nums[j]
                    flag = 1
            if not flag:
                break
        return nums
    
        
        

nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.bubble_sort1(nums))
print(rst.bubble_sort1(nums1))
print(rst.bubble_sort1([]))
print(rst.bubble_sort1([1]))
print(rst.bubble_sort2(nums))
print(rst.bubble_sort2([]))
print(rst.bubble_sort2([1]))
