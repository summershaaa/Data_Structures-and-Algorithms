# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:21:56 2019

@author: WinJX
"""
#剑指50：第一个只出现一次的字符
#在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
#并返回它的位置, 如果没有则返回 -1（需要区分大小写）
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        from collections import Counter
        cnt = Counter(s)
        if 1 in cnt.values():
            for i in s:
                if cnt[i] == 1:
                    return s.index(i)
        return -1
    #相关题目1：输入两个字符串a,b.删除a中b的字符。
    #比如a = 'We are students'.b = 'aeiou'。
    #则结果为'W r stdnts'
    def del_a_str_in_b(self,a,b):
        list_a = list(a)
        list_b = list(b)
        for ch in list_a:
            if ch in list_b:
                list_a.remove(ch)
        return ''.join(list_a)
    
    #相关题目2：删除字符串中所有重复出现的字符，如google --> gole
    def del_same_char(self,string):
        rst = []
        for ch in string:
            if ch not in rst:
                rst.append(ch)
        return ''.join(rst)

    #相关题目3：判断两个单词是互为变位词，即出现的字母和次数相同。bat,tab,abt
    def anagram(self,a,b):
        dic = {}
        for ch in a:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for ch in b:
            if ch not in dic:
                return False
            else:
                dic[ch] -= 1
        val = dic.values()
        return all([x==0 for x in val])
        
    
    
    
result = Solution()
print(result.FirstNotRepeatingChar('abaccdeff'))
print(result.FirstNotRepeatingChar('abbaccddeeff'))
print(result.FirstNotRepeatingChar(''))

print(result.del_a_str_in_b('We are students','aeiou'))

print(result.del_same_char('google'))
print(result.del_same_char('baidu'))

print(result.anagram('bat','tab'))
print(result.anagram('bat','aab'))