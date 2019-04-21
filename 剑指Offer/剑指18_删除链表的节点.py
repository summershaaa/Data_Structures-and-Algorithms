# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:52:13 2019

@author: WinJX
"""

#剑指offer————18:删除链表节点
   
#节点
class Node:
    #单链表节点
    def __init__(self,data,p=None):
        self.data = data
        self.next = p
#    def __del__(self):
#        self.data = None
#        self.next = None

#链表
class Link_List:
    def __init__(self):
        self.head = Node(None)

#    def create(self,data):
#        if len(data) == 0:
#            print('list is null')
#            return
#        self.head.next = Node(data[0])
#        p = self.head.next
#        for i in data[1:]:
#            p.next = Node(i)
#            p = p.next
#
    def print(self):
        p = self.head.next
        while p != None:
            print(p.data,end=' ')
            p = p.next
        print('')


#题目一 在O(1)时间内删除链表节点          
def DeleteNode(LinkList,pToBeDeleted):
    #先判断删除节点的位置，若不是尾节点，则采用覆盖方式
    #若删除尾节点，且链表只有一个节点，则直接将链表头置为None
    #若删除尾节点且有多个节点，则采用常规方法
    if not isinstance(LinkList,Link_List) or not isinstance(pToBeDeleted,Node):
        return
    if pToBeDeleted.next != None:
        # 若删除的不是尾节点
        temp = pToBeDeleted.next
        pToBeDeleted.data = temp.data
        pToBeDeleted.next = temp.next
    elif LinkList.head.next == pToBeDeleted:
        # 若链表只有一个结点，删除头结点（也就是尾节点）
        LinkList.head.next = None
    else:
        # 若链表很多节点，删除尾节点
        p = LinkList.head.next
        while p.next != pToBeDeleted:
            p = p.next
        p.next = None
    
        
def DeleteDuplication(LinkList):
    if not isinstance(LinkList,Link_List):
        return
    #设置两个节点，pPreNode为当前节点的前一个节点
    pPreNode,pNode = LinkList.head.next,LinkList.head.next    
    
    while pNode.next:
        #找不到重复元素的情况
        if pNode.data != pNode.next.data:
            pPreNode = pNode
            pNode = pNode.next
        #存在重复元素
        else:
            #保存当前节点值，遍历到不重复的值或者节点为空
            temp = pNode.data
            while pNode and pNode.data == temp:
                pNode = pNode.next
            #节点为空的情况
            if pNode == None:
                #若是头部重复 : [1,1],直接置头指针为空
                if pPreNode == None:
                    LinkList.head.next == None
                    return 
                #若数据是[1,2,2]这种尾部重复的话，则让pPreNode.next指向空
                else:
                    pPreNode.next = pNode
                    return 
        #尾部重复
        pPreNode.next = pNode
        
    
# 题目1
#node1 = Node(10)
#node2 = Node(11)
#node3 = Node(13)
#node4 = Node(15)
#node1.next = node2
#node2.next = node3
#node3.next = node4
#S = Link_List()
#S.head.next = node1
#S.print()
#DeleteNode(S,node1)
#S.print()        
        
#题目二测试用例
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(3)
n5 = Node(4)
n6 = Node(4)
n7 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
S = Link_List()
S.head.next = n1
S.print()
DeleteDuplication(S)
S.print()
        
