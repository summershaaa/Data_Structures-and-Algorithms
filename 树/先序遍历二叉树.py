# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:36:35 2019

@author: WinJX
"""

#先序遍历二叉树

class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #递归版本  根左右
    def preorderTraverse1(self,root):
        if not root:
            return None
        print(root.val,end = ' ')
        self.preorderTraverse1(root.left)
        self.preorderTraverse1(root.right)
        
    """非递归方法
    1,访问当前节点，若有右子树将右子树入栈
    2，继续访问左子树，每访问时都将右子树入栈
    3，若左子树为空，则将节点改为栈顶元素(其右兄弟节点)
    """
    def preorderTraverse2(self,root):
        if not root:
            return None
        stack = []
        while root or stack:
            while root:
                print(root.val,end = ' ')
                stack.append(root.right)
                root = root.left
            root = stack.pop()

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print("递归先序")
rst.preorderTraverse1(root)
print()
print("*************")
print("非递归先序")
rst.preorderTraverse2(root)