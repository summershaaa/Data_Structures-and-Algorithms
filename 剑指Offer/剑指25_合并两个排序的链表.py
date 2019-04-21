# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:40:34 2019

@author: WinJX
"""
#剑指offer-25 : 合并两个排序的链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.Merge(pHead1,pHead2.next)
        return pMergedHead
    
#        rst = tmp = ListNode(None)
#        while pHead1 and pHead2:
#            if pHead1.val < pHead2.val:
#                tmp.next = pHead1
#                pHead1 = pHead1.next
#            else:
#                tmp.next = pHead2
#                pHead2 = pHead2.next
#            tmp = tmp.next
#        tmp.next = pHead1 or pHead2
#        return rst.next
        
    

pHead1 = ListNode(1)
tmp1 = pHead1
for i in [3,5,7]:
    tmp1.next = ListNode(i)
    tmp1 = tmp1.next
pHead2 =  ListNode(2)
tmp2 = pHead2
for j in [4,6,8]:
    tmp2.next = ListNode(j)
    tmp2 = tmp2.next
rst = Solution()
print(rst.Merge(pHead1,pHead2))
