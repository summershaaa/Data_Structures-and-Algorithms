# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:02:49 2019

@author: WinJX
"""
#剑指14： 剪绳子

class Solution:
    #动态规划
    def max_product_after_cuting1(self,length):
        
        if length < 2:
            return 0
        if length == 2:
            return 2
        if length == 3:
            return 3
        product = [0]*(length+1)
        product[0] = 0
        product[1] = 1
        product[2] = 2
        product[3] = 3
        max_product = 0
        
        for i in range(4,length+1):
            for j in range(1,i//2+1):
                temp = product[j]*product[i-j]
                if temp > max_product:
                    max_product = temp
                product[i] = max_product
        return product[length]
    
    #贪心算法
    def max_product_after_cuting2(self,length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        #尽可能多地去剪长度为3的绳子段
        times_of_3 = length//3
        #当绳子最后剩下的长度为4的时候，不能再剪去长度为3的绳子段
        #更好的办法是把绳子剪成长度为2的两端，即2*2>3*1
        if length - times_of_3 == 1:
            times_of_3 -= 1
        times_of_2 = (length -times_of_3*3)//2
        return pow(3,times_of_3)*pow(2,times_of_2)
        
    
    

rst = Solution()
length = 8
print(rst.max_product_after_cuting1(length))
print(rst.max_product_after_cuting2(length))
print(rst.max_product_after_cuting1(0))
print(rst.max_product_after_cuting1(1))
print(rst.max_product_after_cuting1(2))
print(rst.max_product_after_cuting1(3))
print(rst.max_product_after_cuting1(4))



