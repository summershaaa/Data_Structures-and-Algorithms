# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:31:29 2019

@author: WinJX
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:
            
            res.append([root.val]+i)
        return res
rst = Solution()
root = TreeNode(10)
node5 = TreeNode(5)
node12 = TreeNode(12)
node4 = TreeNode(4)
node7 = TreeNode(7)
root.left = node5
root.right = node12
node5.left = node4
node5.right = node7
print(rst.FindPath(root,22))