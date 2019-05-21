# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:18:35 2019

@author: WinJX
"""
#剑指38：字符串的排列


class Solution:
    def Permutation(self, ss):
        # write code here
#        from itertools import permutations
#        if not ss:
#            return []
#        length = len(ss)
#        rst = permutations(ss,length)
#        return [''.join(x) for x in sorted(list(set(rst)))]
        if not ss:
            return []
        rst = []
        self.recursion(rst,0,list(ss))
        rst.sort()
        return rst
    def recursion(self,rst,idx,string):
        if idx == len(string)-1:
            if ''.join(string) not in rst:
                rst.append(''.join(string))
        else:
            for i in range(idx,len(string)):
                string[i],string[idx] = string[idx],string[i]
                self.recursion(rst,idx+1,string)
                string[i],string[idx] = string[idx],string[i]
                

rst = Solution()
print(rst.Permutation('abc'))
print(rst.Permutation('aa'))
print(rst.Permutation(''))
print(rst.Permutation('aabb'))