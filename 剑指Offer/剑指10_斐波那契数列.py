# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:34:10 2019

@author: WinJX
"""

#剑指10:斐波那契数列
class Solution:
    #求斐波那契数列的第N项
    #题目2：青蛙跳台阶问题
    def Fibonacci(self,n):
#        if n==0:
#            return 0
#        if n==1:
#            return 1
#        return self.Fibonacci(n-2)+self.Fibonacci(n-1)
        
        if n <=1:
            return n
        a,b = 0,1
        for i in range(2,n+1):
            a,b = b,a+b
        return b
    

    #题目3：矩形覆盖
    def rectCover(self, number):
        if number <= 0:
            return 0
        dp = [0]*(number+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,number+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[number]
        
        
rst = Solution()
print(rst.Fibonacci(9))
print(rst.rectCover(8))