# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:49:15 2019

@author: WinJX
"""

'''希尔排序'''

def shell_sort(lst):
    gap = len(lst)//2
    while gap > 0:
        for i in range(gap,len(lst)):
            while i-gap >= 0 and lst[i] < lst[i-gap]:
                lst[i],lst[i-gap] = lst[i-gap],lst[i]
                i -= gap
        gap = gap//2
    return lst
        
