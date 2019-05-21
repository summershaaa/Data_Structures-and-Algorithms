# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:09:43 2019

@author: WinJX
"""

class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        deque = [root]
        rst = []
        while deque:
            tmp = deque.pop(0)
            rst.append(tmp.val)
            if tmp.left:
                deque.append(tmp.left)
            if tmp.right:
                deque.append(tmp.right)
        return rst
    
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        rst = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                root = queue.pop(0)
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            rst.append(tmp)
        return rst
    #按Z字形打印
    def PrintByZ(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        rst = []
        level = 1
        while stack:
            temp_stack = []
            temp_rst = []
            for root in stack:
                if root:
                    temp_rst.append(root.val)
                if root.left:
                    temp_stack.append(root.left)
                if root.right:
                    temp_stack.append(root.right)
            if level&1==0:
                temp_rst.reverse()
            if temp_rst:
                rst.append(temp_rst)
            
            level += 1
            stack = temp_stack
        return rst
            
            
            

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print(rst.PrintFromTopToBottom(root))
print(rst.Print(root))
print(rst.PrintByZ(root))