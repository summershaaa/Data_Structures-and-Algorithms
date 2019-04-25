# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:52:22 2019

@author: WinJX
"""
#中序遍历二叉树

class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #递归方法  左根右
    def inorderTraverse1(self,root):
        if not root:
            return None 
        self.inorderTraverse1(root.left)
        print(root.val,end = ' ')
        self.inorderTraverse1(root.right)
        
    """非递归方法
    1,将当前节点入栈且将节点置为其左子树
    2,若左子树空，但栈不空，则弹出栈顶元素，访问栈顶元素后将节点置为其右子树
    """
    def inorderTraverse2(self,root):
        if not root:
            return None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                print(root.val,end = ' ')
                root = root.right
            

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print("递归中序")
rst.inorderTraverse1(root)
print()
print("*************")
print("非递归中序")
rst.inorderTraverse2(root)