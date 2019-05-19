# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:32:32 2019

@author: WinJX
"""

class Solution:
    def Heap_Sort(self,nums):
        if len(nums) <= 1:
            return nums
        length = len(nums)
        
        #创建初始最大堆，从最后一个父节点到根节点
        for i in range(length//2-1,-1,-1):
            self.sift(nums,i,length-1)
            
        #挨个把根节点值与最后一个节点值交换
        for i in range(length-1,-1,-1):
            #交换位置
            nums[i],nums[0] = nums[0],nums[i]
            #继续调整堆，从根节点开始，此时堆的数量变少，因为移到最后的较大值不参与调整了
            self.sift(nums,0,i-1)
        return nums
    
    def sift(self,nums,parent,length):
        child = 2*parent+1
        parent_value = nums[parent]
        
        #孩子节点位置要在堆容量内
        while child <= length:
            #如果child<length，说明存在右孩子
            if child < length and nums[child] < nums[child+1]:
                child += 1   #找到孩子节点值大的索引
            #父节点值与较大孩子值比较
            if parent_value > nums[child]:
                break   #父节点值大，直接跳出
            else:
                #交换父节点和孩子系欸但值，并更新父节点孩子节点位置
                nums[parent] = nums[child]
                parent = child
                child = 2*parent+1
        #在循环退出后，如果父节点和孩子节点没有交换过，这个赋值语句啥也没做，
        #但如果发生交换了，parent位于值较大孩子处，则退出循环后父节点的值
        #已经是孩子节点中的较值大。所以还需要把最开始保存的父节点值赋值给较大值的孩子节点
        nums[parent] = parent_value
        """
        23               45                45
       /  \    -->      /  \      -->     / \
      12  45           12   45          12  23
      
      parent_value = 23,nums[child] = 45  parent = child   
      先把 45 移到 23的位置，然后把nums[parent]的值(45)改为parent_value(23)
        """
        
        
nums = [24,54,23,6,12,12,45,2]
nums1 = [51,45,37,35,25,25,12,4]
rst = Solution()
print(rst.Heap_Sort(nums))
print(rst.Heap_Sort(nums1))
print(rst.Heap_Sort([]))
print(rst.Heap_Sort([1]))
        
                