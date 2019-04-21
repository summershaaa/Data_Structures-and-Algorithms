# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:04:38 2019

@author: WinJX
"""

'''选择排序'''

def select_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
print(select_sort([2,54,21,54,24,57,34]))