# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:37:32 2019

@author: WinJX
"""
#剑指57：和为s的数字
class Solution:
    #题目1：和为s的两个数字
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        
#        for i in range(len(array)):
#            diff = tsum - array[i]
#            if diff in array[:i]+array[i+1:]:
#                rst = [array[i],diff]
#                return sorted(rst)
#            else:
#                continue
#        return []
        if len(array) < 2:
            return []
        left,right = 0,len(array)-1
        while left < right:
            temp = array[left]+array[right]
            if temp == tsum:
                return [array[left],array[right]]
            elif temp < tsum:
                left += 1
            else:
                right -= 1
        return []
    
    #题目2：和为s的连续正数序列
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        left,right = 1,2
        mid = (1+tsum)//2
        rst = []
        cur_sum = sum(range(left,right+1))
        while left < mid:
            if cur_sum == tsum:
                rst.append(list(range(left,right+1)))
                right += 1
                cur_sum += right
            elif cur_sum > tsum:
                cur_sum -= left
                left += 1
            else:
                right += 1
                cur_sum += right
        return rst
#        while left < mid:
#            if cur_sum == tsum:
#                rst.append(list(range(left,right+1)))
#            while cur_sum > tsum and left < mid:
#                cur_sum -= left
#                left += 1
#                if cur_sum == tsum:
#                    rst.append(list(range(left,right+1)))
#            right += 1
#            cur_sum += right
#        return rst
            
        
        
        

rst = Solution()
print(rst.FindNumbersWithSum([1,2,4,7,11,15],11))
print(rst.FindContinuousSequence(100))