# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:21:24 2019

@author: WinJX
"""
#剑指37：序列化二叉树

class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
        
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)
    
    def Deserialize(self, s):
        # write code here
        l = s.split(',')
        return self.d(l)
    
    def d(self,l):
        if len(l)<=0:
            return None
        val = l.pop(0)
        root = None
        if val!='#':
            root = TreeNode(int(val))
            root.left = self.d(l)
            root.right = self.d(l)
        return root
rst = Solution()
root = TreeNode(8,TreeNode(6,TreeNode(5),TreeNode(7)),TreeNode(6,TreeNode(7),TreeNode(5)))
print(rst.Serialize(root))
s = '8,6,5,#,#,7,#,#,6,7,#,#,5,#,#'
print(rst.Deserialize(s))