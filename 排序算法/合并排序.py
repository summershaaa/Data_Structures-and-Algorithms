# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:15:53 2019

@author: WinJX
"""

'''合并排序'''

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        mid = len(nums)//2
        nums_l = merge_sort(nums[:mid])
        nums_r = merge_sort(nums[mid:])
    return merge(nums_l,nums_r)

def merge(left,right):
    l,r = 0,0
    rst = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            rst.append(left[l])
            l += 1
        else:
            rst.append(right[r])
            r += 1
    rst += left[l:]
    rst += right[r:]
    return rst
    
