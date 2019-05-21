# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:12:27 2019

@author: WinJX
"""
#剑指36：二叉搜索树与双向链表

class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
  
        # 连接根与左子树最大结点
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree
  
        # 处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
  
        # 连接根与右子树最小结点
        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
              
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

rst = Solution() 
root = TreeNode(10,TreeNode(6,TreeNode(4),TreeNode(8)),TreeNode(14,TreeNode(12),TreeNode(16)))
print(rst.Convert(root))