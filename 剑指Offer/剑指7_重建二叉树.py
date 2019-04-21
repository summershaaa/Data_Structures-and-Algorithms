# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:07:23 2019

@author: WinJX
"""
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

#重建二叉树
#第一种，已知前序和中序遍历结果
class Solution:
    def buildTree1(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree1(preorder[1:1+index],inorder[:index])
        root.right = self.buildTree1(preorder[1+index:],inorder[1+index:])
        return root
        
#第二种，已知中序和后序遍历结果
    def buildTree2(self,inorder,postorder):
        if not postorder:
            return 
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree2(inorder[:index],postorder[:index])
        root.right = self.buildTree2(inorder[index+1:],postorder[index:-1])
        return root
    
    
pre = [1,2,4,7,3,5,6,8]
ino = [4,7,2,1,5,3,8,6]
post = [7,4,2,5,8,6,3,1]
rst = Solution()
rst.buildTree1(pre,ino)
rst.buildTree2(ino,post)
