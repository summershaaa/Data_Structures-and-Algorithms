# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:43:14 2019

@author: WinJX
"""

#剑指28：对称的二叉树
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
    
class Solution:
    
    def isSymmetrical(self,root):
        if not root:
            return True
        return self.isSymmetrical_core(root,root)
    
    def isSymmetrical_core(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isSymmetrical_core(root1.left,root2.right) and \
               self.isSymmetrical_core(root1.right,root2.left)
              
root = TreeNode(8,TreeNode(6,TreeNode(5),TreeNode(7)),TreeNode(6,TreeNode(7),TreeNode(5)))
root1 = TreeNode(7,TreeNode(7,TreeNode(7),TreeNode(7)),TreeNode(7,TreeNode(7)))
rst = Solution()
print(rst.isSymmetrical(root))
print(rst.isSymmetrical(root1))