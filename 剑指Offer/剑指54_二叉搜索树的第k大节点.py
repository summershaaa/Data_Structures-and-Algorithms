# -*- coding: utf-8 -*-
"""
Created on Fri May  3 20:07:45 2019

@author: WinJX
"""
#剑指54：二叉搜索树的第K小节点

class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
        
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k<=0:
            return 
        stack = []
        rst = []
        while pRoot or stack:
            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left
            if stack:
                pRoot = stack.pop()
                rst.append(pRoot.val)
                pRoot = pRoot.right
        return rst[k-1]
rst = Solution()
pRoot = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
print(rst.KthNode(pRoot,3))
                