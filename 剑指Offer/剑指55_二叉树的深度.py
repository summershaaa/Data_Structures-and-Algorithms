# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:33:32 2019

@author: WinJX
"""
#剑指55：二叉树的深度

class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)
        return max(depth_left,depth_right)+1
    
    #题目2：平衡二叉树
    def IsBalanced(self,pRoot):
        if not pRoot:
            return True
        depth_left = self.TreeDepth(pRoot.left)
        depth_right = self.TreeDepth(pRoot.right)
        #左右子树高度差
        diff = abs(depth_left-depth_right)
        #超过1则不是平衡二叉树
        if diff > 1:
            return False
        return self.IsBalanced(pRoot.left) and self.IsBalanced(pRoot.right)
        
        
pRoot = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(7))),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print(rst.TreeDepth(pRoot))
print(rst.IsBalanced(pRoot))