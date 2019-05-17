# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:15:52 2019

@author: WinJX
"""

#剑指9 ：用两个栈实现队列
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
尾部插入到stack1中
删除：如果stack2为空，若stack1不空，则把stack1中元素弹出并压入stack2中，
直到stack1为空，则弹出stack2栈顶元素。

"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()
    
rst = Solution()
rst.push(1)
rst.push(2)
print(rst.pop())
rst.push(3)
print(rst.pop())
