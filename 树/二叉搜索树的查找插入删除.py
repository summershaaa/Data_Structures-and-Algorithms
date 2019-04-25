# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:54 2019

@author: WinJX
"""

#二叉搜索树的查找
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    
    #统计二叉树节点个数
    def count_Node(self,root):
        if not root:
            return 0
        else:
            return 1 + self.count_Node(root.left)+self.count_Node(root.right)

    #对树节点求和
    def sum_Node(self,root):
        if not root:
            return 0
        else:
            return root.val + self.sum_Node(root.left) + self.sum_Node(root.right)
    
    #查找
    def find(self,root,value):        
        while root:
            if value > root.val:
                root = root.right
            elif value < root.val:
                root = root.left
            else:
                return root
        return None
#        if not root:
#            return None
#        if value > root.val:
#            return self.find(value,root.right)
#        elif value < root.val:
#            return self.find(value,root.left)
#        else:
#            return root
        
    
    #最小查找：查找二叉树最小的元素
    def findMin(self,root):
        if not root:
            return None
        while root.left:
                root = root.left               
        return root
        
    #最大查找：查找二叉树最大的元素
    def findMax(self,root):
        if not root:
            return 
        if root.right:
            return self.findMax(root.right)
        else:
            return root
        
    #插入
    def Insert(self,root,value):
        if not root:
            root = TreeNode(value)
        elif value > root.val:
            root.right = self.Insert(root.right,value)
        elif value < root.val:
            root.left = self.Insert(root.left,value)
        return root
    #删除
    def Delete(self,root,value):
        if not root:
            return None
        if value < root.val:
            root.left = self.Delete(root.left,value)
        elif value > root.val:
            root.right = self.Delete(root.right,value)
        #分三种情况    
        else:
            #1.既有左子树又有右子树,找到右子树中值最小的节点,将该值赋给root,再把该节点删除
            if root.left and root.right:
                tmp = self.findMin(root.right)
                root.val = tmp.val
                root.right = self.Delete(root.right,tmp.val)
         
                 #存在左子树或者右子树，用其子树代替即可
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
                
            #3.左右子树都为空，直接删除
            elif not root.left and not root.right:
                root = None
        return root
        
root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
rst = Solution()
print("二叉搜索树节点个数",rst.count_Node(root))
print("二叉树搜索树节点和",rst.sum_Node(root))
print("二叉搜索树的查找",rst.find(root,3).val)
print("二叉搜索树的最小值",rst.findMin(root).val)
print("二叉搜索树的最大值",rst.findMax(root).val)
print("插入节点1：",rst.Insert(root,1))
print("二叉树搜索树节点和",rst.sum_Node(root))
print('删除节点1：',rst.Delete(root,1))
print("二叉树搜索树节点和",rst.sum_Node(root))

