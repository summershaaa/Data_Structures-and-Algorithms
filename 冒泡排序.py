# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:15:38 2019

@author: WinJX
"""

'''冒泡排序'''
def bubble_sort(nums):
    for i in range(len(nums)-1):
        target = True
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                target = False
        if target:
            break
    return nums
print(bubble_sort([2,43,21,54,22,1,65]))