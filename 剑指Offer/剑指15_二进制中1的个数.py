# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:19:52 2019

@author: WinJX
"""

#剑指15_二进制中1的个数
"""
把一个整数减去1后再和原来的整数做位与运算，得到的结果相当于把整数
的二进制表示中最右边的1编程0.  12&11 == 8   1100 & 1011 = 0100
"""

class Solution:
    def NumberOf1(self, n):
        # write code here
        #因为python中整数时没有限制位数的，所以要对负数做处理
        if n < 0:
            n &=0xffffffff 
       # cnt = 0
#        while n:
#            #与1做与运算
#            if n&1:
#                cnt += 1
#            #右移
#            n = n>>1
#        return cnt
        return sum([n>>i & 1 for i in range(32)])
    
    #相关题目：判断一个整数是不是2大的整数次方
    #2的整数次方n只有一位是1，且其他位都是0，
    #可以将n减一再和n做与操作，n&(n-1)==0则n是2的整数次方
    def pow_of_2(self,n):
        if n <= 0:
            return False
        return not n&(n-1)
    
    #两个整数m和n,计算需要改变m的二进制多数位才能得到n，
    #如m,n=10,13 .  10 :1010,13:1101,则需要改变三次
    def change_count(self,m,n):
        #先进行异或，再计算异或结果中1的个数
        ans = m^n
        return self.NumberOf1(ans)
        
                
rst = Solution()
print(rst.NumberOf1(0))
print(rst.NumberOf1(1))
print(rst.NumberOf1(0x7fffffff))
print(rst.NumberOf1(0xffffffff))
print(rst.NumberOf1(0x80000000))

print(rst.pow_of_2(0))
print(rst.pow_of_2(-2))
print(rst.pow_of_2(2))
print(rst.pow_of_2(1))
print(rst.pow_of_2(3))

print(rst.change_count(10,13))
