# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:28:44 2019

@author: WinJX
"""

#剑指29：顺时针打印矩阵
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        col = len(matrix[0])
        row = len(matrix)
        if not matrix or col<=0 or row<=0:
            return 
        start = 0  #起始行列号
        rst = []
        while col > start*2 and row > start*2:
            self.printMatrixInCircle(matrix,col,row,start,rst)
            start += 1
        return rst
    
    def printMatrixInCircle(self,matrix,col,row,start,rst):
        end_X = col - start -1   #终止列号
        end_Y = row - start -1   #终止行号
        
        #从左到右：肯定需要，注意控制边界条件
        for i in range(start,end_X+1):
            rst.append(matrix[start][i])
        
        #从上到下：满足终止行号大于起始行号
        if start < end_Y:
            for i in range(start+1,end_Y+1):
                rst.append(matrix[i][end_X])
        
        #从右到左：至少两行两列，即终止行列号都大于起始行列号
        if start < end_X and start < end_Y:
            for i in range(end_X-1,start-1,-1):
                rst.append(matrix[end_Y][i])
                
        #从下往上：至少三行两列，即终止列号大于起始行号，终止列号大于起始列号+1
        if start < end_X and start < end_Y-1:
            for i in range(end_Y-1,start,-1):
                rst.append(matrix[i][start])

rst = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix1 = [[1,2,3,4]]
matrix2 = [[1],[2],[3],[4]]
matrix3 = [[1]]
print(rst.printMatrix(matrix))
print(rst.printMatrix(matrix1))
print(rst.printMatrix(matrix2))
print(rst.printMatrix(matrix3))
        