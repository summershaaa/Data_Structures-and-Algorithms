# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:36:22 2019

@author: WinJX
"""

#剑指21：调整数组顺序使奇数位于偶数前面
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        #return sorted(array,key = lambda x:x&1,reverse = True)
        
        stack1 = [x for x in array if x&1]
        stack2 = [x for x in array if x&1==0]
        return stack1+stack2
    
        