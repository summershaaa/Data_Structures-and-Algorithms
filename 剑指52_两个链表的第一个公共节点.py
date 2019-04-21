# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:15:25 2019

@author: WinJX
"""

#剑指offer__52：两个链表的第一个公共节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
#        list1 = []
#        node1 = pHead1
#        node2 = pHead2
#        while node1:
#            list1.append(node1.val)
#            node1 = node1.next
#        while node2:
#            if node2.val in list1:
#                return node2
#            else:
#                node2 = node2.next
 
        
#        stack1 = []
#        stack2 = []
#        node1 = pHead1
#        node2 = pHead2
#        while node1:
#            stack1.insert(0,node1)
#            node1 = node1.next
#        while node2:
#            stack2.insert(0,node2)
#            node2 = node2.next
#        idx = 0
#        while stack1[idx] == stack2[idx]:
#            idx += 1
#        return stack1[idx-1].val
        p1_len = self.getLength(pHead1)
        p2_len = self.getLength(pHead2)
        sub_len = abs(p1_len - p2_len)
        p1 = pHead1
        p2 = pHead2
        if p1_len > p2_len:
            for i in range(sub_len):
                p1 = p1.next
        else:
            for i in range(sub_len):
                p2 = p2.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
            
        
        
    def getLength(self,Head):
        p = Head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        return cnt
        
        
        
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next=node2
node2.next=node3
node3.next=node6
node6.next=node7
node4.next=node5
node5.next=node6

a2 = Solution()
b = a2.FindFirstCommonNode(node1,node4)
print(b)