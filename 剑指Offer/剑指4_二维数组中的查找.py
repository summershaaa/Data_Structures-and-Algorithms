# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:50:54 2019

@author: WinJX
"""
#剑指4 ： 二维数组中的查找

"""
选取数组右上角元素get 与 target 作比较
1:如果get == target,返回True
2:如果get > target ,则去除get所在列，即col--
3:如果get < target ,则去除get所在行，即row++
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows = len(array)-1     #数组行数
        col = len(array[0])-1 #数组列数
        row = 0
        while row <= rows and col>=0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    
rst = Solution()
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(rst.Find(7,array))
print(rst.Find(3,array))
print(rst.Find(0,array))
        