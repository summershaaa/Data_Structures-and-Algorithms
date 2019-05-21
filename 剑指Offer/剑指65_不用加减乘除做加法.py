# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:54:58 2019

@author: WinJX
"""
#剑指65：不用加减乘除做加法

class Solution:
    def Add(self, num1, num2):
        # write code here
        carry = num1&num2
        while carry:
            rst = num1^num2  #不算进位的求和
            carry = (num1&num2)<<1 #进位
            num1,num2 = rst,carry
        return num1
if __name__ == '__main__':
    rst = Solution()
    print(rst.Add(5,17))