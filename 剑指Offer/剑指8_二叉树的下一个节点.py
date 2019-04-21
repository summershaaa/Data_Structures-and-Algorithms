# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:41:27 2019

@author: WinJX
"""
#

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  #指向父亲节点
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return 
        #存在右子树，下一个节点就是右子树最左子节点
        if pNode.right:
            rst = pNode.right
            while rst.left:
                rst = rst.left
            return rst
        #不存在右子树
        while pNode.next:
            tmp = pNode.next
            #节点是它父亲点的左子节点，下一个节点就是它的父亲节点，
            #否则一直向上遍历知道一个是它父节点的左子节点的节点。
            if tmp.left == pNode:
                return tmp
            pNode = tmp
        return None

a = TreeLinkNode('a')
b = TreeLinkNode('b')
c = TreeLinkNode('c')
d = TreeLinkNode('d')
e = TreeLinkNode('e')
f = TreeLinkNode('f')
g = TreeLinkNode('g')
h = TreeLinkNode('h')
i = TreeLinkNode('i')
a.left = b
a.right = c
b.left = d
b.right = e
b.next = a
c.left = f
c.right = g
c.next = a
d.next = b 
e.left = h
e.right = i
e.next = b
f.next = c
g.next = c
h.next = e
i.next = e

rst = Solution()
rst.GetNext(a)


