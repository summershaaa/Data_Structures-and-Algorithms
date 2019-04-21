# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:12:50 2019

@author: WinJX
"""
def sift(nums, parent, length):
    child = 2 * parent + 1     #左子节点索引
    temp = nums[parent]        # 保存父节点值
    while child <= length:    
                               #存在右子节点且值比左子节点值大
        if child < length and nums[child] < nums[child+1]:  
            child += 1         #将索引指向值大的子节点
        if temp > nums[child]: #如果父节点的值大，则跳出
            break
        else:                
            nums[parent] = nums[child]   # 将父节点替换成新的子节点（值大的那个）的值
            parent = child               # 变成新的父节点
            child = 2 * parent + 1       # 新的子节点
    nums[parent] = temp        # 将替换的父节点值赋给最终的父节点


def heap_sort(nums):
    n = len(nums)
    # 创建堆
    for i in range(n//2-1, -1, -1):
        sift(nums, i, n-1)

    # 挨个出数
    for i in range(n-1, -1, -1):    # 从大到小
        nums[0], nums[i] = nums[i], nums[0]     # 将最后一个值与父节点交互位置
        sift(nums, 0, i-1)
    return nums
