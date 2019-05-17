# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
#法一：循环+栈
#    def printListFromTailToHead(self, listNode):
#        # write code here
#        stack = []
#        p = listNode
#        while p:
#            stack.insert(0,p.val)
#            p = p.next
#        return stack
    
#法二：使用递归    
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []       
        return self.printListFromTailToHead(listNode.next)+[listNode.val]
   
    
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

r = Solution()
#测试样例：功能测试：有多个节点，只有一个节点
         #特殊输入测试：链表为空
listnode = CreateList(6)
print(r.printListFromTailToHead(listnode))
listnode = CreateList(0)
print(r.printListFromTailToHead(listnode))
listnode = CreateList(1)
print(r.printListFromTailToHead(listnode))