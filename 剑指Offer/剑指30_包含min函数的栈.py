# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:54:49 2019

@author: WinJX
"""
#剑指30：包含min函数的栈

class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
            
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]

rst = Solution()
rst.push(3)
print(rst.min())
rst.push(4)
print(rst.min())
rst.push(2)
print(rst.min())
rst.push(1)
print(rst.min())
rst.pop()
print(rst.min())
rst.pop()
print(rst.min())
rst.push(0)
print(rst.min())
