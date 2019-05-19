# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:49:49 2019

@author: WinJX
"""
import random
class Solution:
    
    def QuickSort(self,nums,left,right):
#        if left > right:
#            return nums
#        pivot = nums[left]
#        start = left
#        end = right
#        while start < end:
#            while start < end and pivot <= nums[end]:
#                end -= 1
#            nums[start] = nums[end]
#            while start < end and pivot >= nums[start]:
#                start += 1
#            nums[end] = nums[start]
#        nums[start] = pivot
#        self.QuickSort(nums,left,start-1)
#        self.QuickSort(nums,start+1,right)
#        return nums
        if left > right:
            return nums
        pivot = nums[left] #random.randint(left,right)
        start,end = left,right
        while start < end:
            while start < end and pivot <= nums[end]:
                end -= 1
            nums[start] = nums[end]
            
            while start < end and pivot >= nums[start]:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        self.QuickSort(nums,left,start-1)
        self.QuickSort(nums,start+1,right)
        return nums
        
    
#    def Partition(self,nums,left,right):
#        pivot = random.randint(left,right)
#        start,end = left,right
#        while start < end:
#            while start < end and nums[pivot] < nums[end]:
#                end -= 1
#            nums[start] = nums[end]
#            
#            while start < end and nums[pivot] > nums[start]:
#                start += 1
#            nums[end] = nums[start]
#        nums[start] = nums[pivot]
#        return start

lst = [21,5,23,56,2,65]
nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.QuickSort(nums,0,7))
print(rst.QuickSort(lst,0,5))
#print(rst.QuickSort([]))
#print(rst.QuickSort([1]))
        