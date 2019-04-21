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

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print(rst.PrintFromTopToBottom(root))
