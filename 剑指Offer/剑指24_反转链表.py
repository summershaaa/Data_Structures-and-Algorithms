# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:57:45 2019

@author: WinJX
"""

#剑指offer-24 ： 反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        #三指针交换
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead
    
n1 = ListNode(1)
tmp = n1
for i in range(2,7):
    tmp.next = ListNode(i)
    tmp = tmp.next
rst = Solution()
print(rst.ReverseList(n1))
