# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:05:29 2019

@author: WinJX
"""
#剑指51：数组中的逆序对
class Solution:
    def __init__(self):
        self.count = 0
    def InversePairs(self, data):
        # write code here
        if not data:
            return 
        self.InverseCore(data)
        return self.count%1000000007
         
    def InverseCore(self, data):
        if len(data) == 1:
            return data
        mid = len(data)//2
        left = self.InverseCore(data[:mid])
        right = self.InverseCore(data[mid:])
        res, l, r = [], 0, 0
        while l <len(left) and r<len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
                self.count += len(left) - l
        res += left[l:]
        res += right[r:]
        return res

result = Solution()
print(result.InversePairs([7,5,6,4]))