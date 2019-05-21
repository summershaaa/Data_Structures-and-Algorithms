# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:28:03 2019

@author: WinJX
"""
"""
剑指39：数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
#        if not numbers:
#            return 0
#        from collections import Counter
#        cnt = Counter(numbers)
#        rst = cnt.most_common(1)
#        if rst[0][1] > len(numbers)/2:
#            return rst[0][0]
#        else:
#            return 0
        if not numbers:
            return 0
        rst = numbers[0]
        count = 1
        for i in range(1,len(numbers)):
            if count == 0:
                rst = numbers[i]
                count = 1
            elif rst == numbers[i]:
                count += 1
            else:
                count -= 1
            print(rst,count)
        if numbers.count(rst) <= len(numbers)/2:
            return 0
        return rst
            
        
        
    
rst = Solution()
n1 = [1,2,3,2,2,2,5,4,2]
n2 = []
n3 = [1,2,2,1,3]
print(rst.MoreThanHalfNum_Solution(n1))
print(rst.MoreThanHalfNum_Solution(n2))
print(rst.MoreThanHalfNum_Solution(n3))