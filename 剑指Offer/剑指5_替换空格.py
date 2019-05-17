# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:27:21 2019

@author: WinJX
"""
#剑指5 : 替换空格
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution:
    
    # s 源字符串
    def replaceSpace1(self, s):
        # write code here
        return s.replace(' ','%20')
    
    #双指针从后往前移动
    def replaceSpace2(self,s):
        if not s:
            return ""
        s = list(s)
        p1 = len(s) - 1           #p1指针指向原始字符串末尾
        for i in s:               #遇到空格则填充2个长度
            if i == " ":
                s.append(None)
                s.append(None)       
        p2 = len(s) - 1           #p2指向替换后字符串的末尾，长度为 原来长度 + 2*空格数
        #当p1等于p2时，替换完成
        while p1 != p2:
            #如果p1不是空格，则把p1赋给p2,p1和p2同时向前一步
            if s[p1] != " ":
                s[p2] = s[p1]
                p2 -= 1
                p1 -= 1
            #p1为空格，则p2前三格替换为%20，p1向前一步，p2向前3步
            else:
                s[p2-2:p2+1] = ['%','2','0']
                p2 -= 3
                p1 -= 1
        
        return ''.join(s)
           
rst = Solution()
s = 'We are happy'
s1 = ' We are happy ' #首末存在空格
s2 = 'We  are  happy' #存在多个空格
s3 = 'Wearehappy'     #没有空格
s4 = ''               #空字符串
s5 = ' '              #只有一个空格
s6 = '  '             #只有多个空格
print(rst.replaceSpace1(s))
print(rst.replaceSpace2(s1))     
print(rst.replaceSpace2(s2))    
print(rst.replaceSpace2(s3))    
print(rst.replaceSpace2(s4))    
print(rst.replaceSpace2(s5))    
print(rst.replaceSpace2(s6))    
        
