# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:30:07 2019

@author: WinJX
"""

#剑指offer—22 ：链表中倒数第k个节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        #快慢指针法：快指针先走k-1步，然后快慢指针一起走，
        #等快指针为空的时候慢指针刚好在倒数第k位置上
        #要注意判断链表是否为空或者k取值的影响
        if not head or k <= 0:
            return None
        fast = head

        for i in range(k-1):
            if fast.next:
                fast = fast.next
            else:
                return None
        low = head
        while fast.next:
            low = low.next
            fast = fast.next
        return low.val

def CreateList(n):
#链表的创建
    if n <= 0:
        return False
    if n == 1:
        return ListNode(1)
    else:
        listNode = ListNode(1)
        tmp = listNode
        for i in range(2,n+1):
            tmp.next = ListNode(i)
            tmp  = tmp.next
    return listNode

rst = Solution()
n1 = CreateList(6)
print(rst.FindKthToTail(n1,3))