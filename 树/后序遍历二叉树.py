# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:02:07 2019

@author: WinJX
"""

#后序遍历二叉树

class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #递归方法  左根右
    def postorderTraverse1(self,root):
        if not root:
            return None 
        self.postorderTraverse1(root.left)
        self.postorderTraverse1(root.right)
        print(root.val,end = ' ')
        
    """非递归方法
    1,使用两个栈结构，栈1入栈顺序为 左右根，弹出顺序则为根右左
    2,栈1每弹出节点，栈2便存储该节点，则栈2的存储顺序为左右根
    3,顺序访问栈2节点即可
    """
    def postorderTraverse2(self,root):
        stack = [root]
        rst = []
        while stack:
            root = stack.pop()
            rst.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        while rst:
            print(rst.pop(),end = ' ')
            
        
        
        
        #模拟先序遍历根左右，遍历顺序变为根右左，然后逆序输出
#        if not root:
#            return None
#        stack = []
#        rst = []
#        while root or stack:
#            while root:
#               rst.append(root.val)
#               stack.append(root.left)
#               root = root.right
#            root = stack.pop()
#        for i in rst[::-1]:
#            print(i,end = ' ')
        
        
        
        
            

root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
rst = Solution()
print("递归后序")
rst.postorderTraverse1(root)
print()
print("*************")
print("非递归后序")
rst.postorderTraverse2(root)