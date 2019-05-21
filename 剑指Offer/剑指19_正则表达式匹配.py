# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:42:00 2019

@author: WinJX
"""

class Solution:
    def match(self,string, pattern):
        # write code here
        if (len(string) == 0 and len(pattern) == 0):
            return True
        if (len(string) > 0 and len(pattern) == 0):
            return False
        if (len(pattern) > 1 and pattern[1] == '*'):
            if (len(string) > 0 and (string[0] == pattern[0] or pattern[0] == '.')):
                return (self.match(string, pattern[2:]) or self.match(string[1:], pattern[2:]) or self.match(string[1:], pattern))
            else:
                return self.match(string, pattern[2:])
        if (len(string) > 0 and (pattern[0] == '.' or pattern[0] == string[0])):
            return self.match(string[1:], pattern[1:])
        return False
    
rst = Solution()
print(rst.match('aaa','a.a'))
