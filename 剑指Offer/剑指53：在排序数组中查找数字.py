# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:52:22 2019

@author: WinJX
"""
#剑指53：在排序数组中查找数字

class Solution:
    
    #题目一：数字在排序数组中出现的次数
    def GetNumberOfK(self, data, k):
        # write code here
        #return data.count(k)
        #用二分法分别找到第一个k的位置和最后一个k的位置
        if data:
            first_k = self.GetFirstOfK(data,0,len(data)-1,k)
            last_k = self.GetLastOfK(data,0,len(data)-1,k)
            if first_k>-1 and last_k>-1:
                return last_k-first_k+1
        return 0
    
    def GetFirstOfK(self,data,start,end,k):
        if start > end:
            return -1
        mid = (start+end)>>1
        mid_value = data[mid]
        #找到k，判断是不是最左
        if mid_value == k:
            #如果到达最左边界，或者前一位不等于k，则当前为最左的k
            if mid==0 or (mid>0 and data[mid-1] != k):
                return mid
            #否则在前半部分继续查找
            else:
                end = mid -1
        #比k大，则在左半部查找
        elif mid_value > k:
            end = mid-1
        else:  #右半部查找
            start = mid+1
        return self.GetFirstOfK(data,start,end,k)
                
                
    def GetLastOfK(self,data,start,end,k):
        if start > end:
            return -1
        mid = (start+end)>>1
        mid_value = data[mid]
        if mid_value == k:
            #判断是否为最右的k
            if mid == len(data)-1 or (mid<len(data)-1 and data[mid+1] != k):
                return mid
            else:
                start = mid+1
        elif mid_value > k:
            end = mid-1
        else:
            start = mid+1
        return self.GetLastOfK(data,start,end,k)


    #题目2：0~n-1中缺失的数字:长度为n-1的递增排序数组的所有值都是唯一的，
    #且都在0~n-1中，在n个数字中有且只有一个数字不在数组中，找出这个数字
    def GetMissingNumber(self,numbers):
#        #等差数列求和
#        sum_numbers = sum(numbers)
#        length = len(numbers)+1
#        sum_all = (length*(length+1))>>1
#        return sum_all - sum_numbers
#        
        #二分查找，找到第一个下标和对应值不同的数字
        if not numbers:
            return -1
        length = len(numbers)
        left,right = 0,length-1
        while left <= right:
            mid= (left+right)>>1
            if mid != numbers[mid]:
                if mid==0 or numbers[mid-1] == mid-1:
                    return mid
                right = mid-1
            else:
                left = mid+1
        if left == length:
            return length
        return -1
    
    #题目3：数组中数值和下标相等的元素：单调递增唯一
    def GetNumberSameAsIndex(self,numbers):
        if not numbers:
            return -1
        left,right = 0,len(numbers)-1
        while left <= right:
            mid = (left+right)>>1
            if mid == numbers[mid]:
                return mid
            elif mid < numbers[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1
            
        



rst = Solution()
print(rst.GetNumberOfK([1,2,3,3,3,3,4,5],3))
print(rst.GetNumberOfK([1,2,3,3,3,3],3))

print(rst.GetMissingNumber([0,1,2,3,4,5,7,8]))
print(rst.GetNumberSameAsIndex([-3,-1,1,3,5]))