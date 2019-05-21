# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:53:52 2019

@author: WinJX
"""
#剑指20:表示数值的字符串

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s.count('.')>1:
            return False
        allnum = ['0','1','2','3','4','5','6','7','8','9','-','+','.','e','E']
        num = ['0','1','2','3','4','5','6','7','8','9']
        idx = 0
        while idx < len(s):
            if s[idx] not in allnum:
                return False
            if s[idx]=='-' or s[idx]=='+':
                if idx!=0 and s[idx-1]!='e' and s[idx-1]!='E':
                    return False
            if s[idx]=='e' or s[idx]=='e':
                if idx == len(s)-1:
                    return False
                if s[idx+1]=='-' or s[idx+1]=='+':
                    idx += 1
                allnum = num
            idx += 1
        return True
    
rst = Solution()
print(rst.isNumeric('+100'))
print(rst.isNumeric('0'))
print(rst.isNumeric('+5e2'))
print(rst.isNumeric('-1213'))
print(rst.isNumeric('3.134'))
print(rst.isNumeric('1.2.3'))
print(rst.isNumeric('12e'))
print(rst.isNumeric('12e+5.4'))
