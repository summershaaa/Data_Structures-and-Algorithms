# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:53:30 2019

@author: WinJX
"""

'''快速排序'''

def quick_sort(lst,left,right):
    if left > right:
        return lst
    pivot = lst[left]
    start = left
    end = right
    while start < end:
        while start < end and pivot < lst[end]:
            end -= 1
        lst[start] = lst[end]
        while start < end and pivot > lst[start]:
            start += 1
        lst[end] = lst[start]
    lst[start] = pivot
    quick_sort(lst,left,start-1)
    quick_sort(lst,start+1,right)
    return lst
        
lst = [21,5,23,56,2,65]
print(quick_sort(lst,0,5))
