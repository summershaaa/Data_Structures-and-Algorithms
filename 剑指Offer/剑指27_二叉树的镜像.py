# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:26:21 2019

@author: WinJX
"""
#剑指27：二叉树的镜像

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return 
        root.left,root.right = root.right,root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root
    
root = TreeNode(8)
node6 = TreeNode(6)
node10 = TreeNode(10)
node5 = TreeNode(5)
node7 = TreeNode(7)
node9 = TreeNode(9)
node11 = TreeNode(11)
root.left = node6
root.right = node10
node6.left = node5
node6.right = node7
node10.left = node9
node10.right = node11

rst = Solution()
print(rst.Mirror(root))