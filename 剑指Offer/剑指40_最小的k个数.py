# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:45:30 2019

@author: WinJX
"""
#剑指40：最小的k个数

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
#        if not tinput or len(tinput) < k:
#            return []
#        tinput.sort()
#        return tinput[:k]
        
        if k > len(tinput) or k <= 0:
            return []
        index = self.partition(tinput,0,len(tinput)-1)
        while index != k-1:
            if index < k-1:
                index = self.partition(tinput,index+1,len(tinput)-1)
            else:
                index = self.partition(tinput,0,index-1)
        return sorted(tinput[:index+1])
        
    def partition(self,num,l,r):
        pivot = num[r]
        i = l-1
        for j in range(l,r):
            if num[j] <= pivot:
                i += 1
                num[i],num[j] = num[j],num[i]
        num[i+1],num[r] = num[r],num[i+1]
        return i+1
    
    #使用堆
    def GetLeastNumbers_Solution1(self, tinput, k):
        import heapq
        if k > len(tinput) or k <= 0:
            return []
        return heapq.nsmallest(k,tinput)

rst = Solution()
t = [4,5,1,6,2,7,3,8]
t1 = []
t2 = [3,5,1,6]
print(rst.GetLeastNumbers_Solution1(t,4))
print(rst.GetLeastNumbers_Solution1(t1,2))
print(rst.GetLeastNumbers_Solution1(t2,5))
        