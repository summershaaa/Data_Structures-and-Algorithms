# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:50:15 2019

@author: WinJX
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
   
def MeetingNode(pHead):
        if not isinstance(pHead,ListNode) or not pHead:
            return 
        pSlow = pHead
        if not pSlow:
            return 
        pFast = pSlow.next
        while pFast and pFast.next and pFast != pSlow:
            pSlow = pSlow.next
            pFast = pFast.next.next
        if not pFast or not pFast.next:
            return None
        return pFast
     
class Solution:
    
    
    def EntryNodeOfLoop(self, pHead):
        # write code here
        meetingNode = MeetingNode(pHead)
        if not meetingNode:
            return None
        cnt = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            cnt += 1
        pNode1 = pHead
        for i in range(cnt):
            pNode1 = pNode1.next
        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1
    
if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    rst = Solution()
    a = rst.EntryNodeOfLoop(node1)
    print(a.val)