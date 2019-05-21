# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:48:55 2019

@author: WinJX
"""
#剑指26：树的子结构
#输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
        

from operator import eq
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if not pRoot1 or not pRoot2:
            return result
        
        if eq(pRoot1.val,pRoot2.val):
            result = self.DoesTree1HaveTree2(pRoot1,pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left,pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
    
    def DoesTree1HaveTree2(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if not eq(pRoot1.val,pRoot2.val):
            return False
        if eq(pRoot1.val,pRoot2.val):
            return self.DoesTree1HaveTree2(pRoot1.left,pRoot2.left) and \
                   self.DoesTree1HaveTree2(pRoot1.right,pRoot2.right)
                   
tree1 = TreeNode(8,TreeNode(8,TreeNode(9),TreeNode(2,TreeNode(4),TreeNode(7))),TreeNode(7))
tree2 = TreeNode(8,TreeNode(9),TreeNode(2))
rst = Solution()

print(rst.HasSubtree(tree1,tree2))

                   