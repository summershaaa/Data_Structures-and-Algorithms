# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:31:47 2019

@author: WinJX
"""
#归并排序：稳定，时间复杂度O(nlogn)


class Solution:
    
    def Merge_Sort(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)>>1
        left = self.Merge_Sort(nums[:mid])
        right = self.Merge_Sort(nums[mid:])
        return self.Merge(left,right)
    
    def Merge(self,left,right):
        l,r = 0,0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:] or right[r:]
        return result
    
nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.Merge_Sort(nums))
print(rst.Merge_Sort(nums1))
print(rst.Merge_Sort([]))
print(rst.Merge_Sort([1]))