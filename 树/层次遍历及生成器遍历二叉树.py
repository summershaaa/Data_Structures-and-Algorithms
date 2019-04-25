# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:37:09 2019

@author: WinJX
"""

#层次遍历及生成器遍历

class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #层次遍历，借助队列，若队列不空，则出队，并将其左右孩子入队
    def levelTraverse(self,root):
        if not root:
            return None 
        deque = [root]
        while deque:
            root = deque.pop(0)
            print(root.val,end = ' ')
            if root.left:
                deque.append(root.left)
            if root.right:
                deque.append(root.right)
                
        
    """
    生成器先序遍历
    """
    def generatorTraverse(self,root):
        if not root:
            return None
        stack = []
        while root or stack:
            while root:
                stack.append(root.right)
                yield root.val
                root = root.left
            root = stack.pop()

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print("层次遍历")
rst.levelTraverse(root)
print()
print("*************")
print("生成器先序遍历")
generator = rst.generatorTraverse(root)
for i in generator:
    print(i,end = ' ')