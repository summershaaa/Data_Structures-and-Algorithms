# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:19:20 2019

@author: WinJX
"""

#剑指_11： 旋转数组的最小数字

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    #二分思想：O(logn)
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left,right = 0,len(rotateArray)-1
        mid = left
        #是一个旋转数组，且旋转幅度大于0
        while rotateArray[right] <= rotateArray[left]:
            #结束条件，返回right
            if right - left == 1:
                return rotateArray[right]
            #二分
            else:
                mid = (left+right)//2
                #左中右都相等，只能顺序查找
                if rotateArray[left] == rotateArray[mid] and \
                    rotateArray[mid] == rotateArray[right]:
                        return self.min_values(rotateArray)
                   
                #最小数字位于右半部
                if rotateArray[mid] >= rotateArray[left]:
                    left = mid
                #最小数字位于左半部
                elif rotateArray[mid] <= rotateArray[right]:
                    right = mid      
        return rotateArray[mid]
    #顺序查找最小值 O(n)
    def min_values(self,rotateArray):
        min_val = 0
        for val in rotateArray:
            if val < min_val:
                min_val = val
        return min_val
    
rst = Solution()
array = []
array1 = [3,4,5,1,2]
array2 = [1,0,1,1,1]
print(rst.minNumberInRotateArray(array))
print(rst.minNumberInRotateArray(array1))
print(rst.minNumberInRotateArray(array2))

        