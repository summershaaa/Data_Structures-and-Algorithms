# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:18:47 2019

@author: WinJX
"""

#剑指44：数字序列中某一位的数字

class Solution:
    def digitAtIndex(self,index):
        if not index:
            return 0
        count = 1
        num = 0
        while count < index+1:
            num += 1
            count += len(str(num))
            if count >= index+1:
                diff = abs(count - index - len(str(num)))
                return int(str(num)[diff])

rst = Solution()
print(rst.digitAtIndex(1001))
print(rst.digitAtIndex(5))
print(rst.digitAtIndex(10))
print(rst.digitAtIndex(1000))
print(rst.digitAtIndex(999))