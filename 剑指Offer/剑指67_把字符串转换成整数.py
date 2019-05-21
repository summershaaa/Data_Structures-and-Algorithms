# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:22:26 2019

@author: WinJX
"""
#剑指67：把字符串转换成整数

class Solution:
    def StrToInt(self, s):
        # write code here
        
        int_list = ['0','1','2','3','4','5','6','7','8','9','+','-']
        if not s or s[0] not in int_list:
            return 0
        flag = 1  #正负数标记
        total = 0
        
        #判断首位
        if s[0] == '+':
            flag = 1
            s = s[1:]
        elif s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '0':
            s = s[1:]
            
        for ch in s:
            if ch not in int_list:
                return 0
            else:
                total = total*10+int_list.index(ch)
        return flag*total

rst = Solution()
print(rst.StrToInt('+123241'))
print(rst.StrToInt(''))
print(rst.StrToInt('-13'))
print(rst.StrToInt('int'))
print(rst.StrToInt('1234123434223'))
            