# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:33:15 2019

@author: WinJX
"""
#剑指31：栈的压入，弹出序列

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        #辅助栈
        stack = []
        for i in pushV:
            stack.append(i)
            #辅助栈顶元素和弹出序列栈底元素相等时则将其都弹出
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        #辅助栈空表明全部匹配
        return not stack
    
rst = Solution()
push = [1,2,3,4,5]
pop1 = [4,5,3,2,1]
pop2 = [4,5,3,1,2]
print(rst.IsPopOrder(push,pop1))
print(rst.IsPopOrder(push,pop2))