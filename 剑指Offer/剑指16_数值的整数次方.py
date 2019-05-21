# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:05:53 2019

@author: WinJX
"""

#剑指16：数值的整数次方
#给定一个double类型的浮点数base和int类型的整数exponent。
#求base的exponent次方。
class Solution:
    def Power(self, base, exponent):
        # write code here
        if not base and not exponent:
            return None
        unsigned_exponent = exponent if exponent > 0 else abs(exponent)
        rst = self.unsigned_power(base,unsigned_exponent)
        if exponent < 0:
            return 1/rst
        return rst
    
    def unsigned_power(self,base,unsigned_exponent):
#        rst = 1
#        for i in range(1,unsigned_exponent+1):
#            rst *= base
#        return rst
        if unsigned_exponent == 0:
            return 1
        if unsigned_exponent == 1:
            return base
        rst = self.unsigned_power(base,unsigned_exponent>>1)
        rst *= rst
        if unsigned_exponent&1 == 1:
            rst *= base
        return rst
        
    
rst = Solution()
print(rst.Power(2,4))
print(rst.Power(0,4))
print(rst.Power(2,0))
print(rst.Power(0,0))
print(rst.Power(-2,4))
print(rst.Power(2,-4))
