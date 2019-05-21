# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:04:04 2019

@author: WinJX
"""
#翻转单词顺序列
class Solution:
    def ReverseSentence(self, s):
        # write code here
        reversed_s = s.split(' ')[::-1]
        return " ".join(reversed_s)
    
    #左旋转字符串
    def LeftRotateString(self, s, n):
        # write code here
        #return s[n:]+s[:n]  #''.join(list(s[n:])+list(s[:n]))
        #先分别翻转两部分，合并后再整体翻转
        if not s or n<1:
            return s
        left_part = s[:n]
        right_part = s[n:]
        rst = left_part[::-1] + right_part[::-1]
        return rst[::-1]

rst = Solution()
print(rst.ReverseSentence('student. a am I'))
print(rst.ReverseSentence(''))
print(rst.ReverseSentence(' '))

print(rst.LeftRotateString('abcdefg',2))
print(rst.LeftRotateString('',0))

