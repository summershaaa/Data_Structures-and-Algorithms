# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:58:47 2019

@author: WinJX
"""
#剑指35：复杂链表的复制

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
#解题思路：
#1、遍历链表，复制每个结点，如复制结点A得到A1，将结点A1插到结点A后面；
#2、重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
#3、拆分链表，将链表拆分为原链表和复制后的链表
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead: return None
        cur = pHead
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = pHead
        while cur:
            tmp = cur.next
            if cur.random:
                tmp.random = cur.random.next
            cur = tmp.next
        cur = pHead
        res = pHead.next
        while cur.next:
            tmp = cur.next
            cur.next = tmp.next
            cur = tmp
        return res
rst = Solution()
a = RandomListNode('A')
b = RandomListNode('B')
c = RandomListNode('C')
d = RandomListNode('D')
e = RandomListNode('E')
a.next = b
b.next = c
c.next = d
d.next = e
a.random = c
b.random = e
d.random = b
print(rst.Clone(a))