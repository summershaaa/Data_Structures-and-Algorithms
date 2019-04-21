# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:20:10 2019

@author: WinJX
"""

'''插入排序'''

def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
    return nums
print(insert_sort([3,12,4,12,245,234]))
