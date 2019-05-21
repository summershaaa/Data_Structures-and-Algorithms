# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:58:23 2019

@author: WinJX
"""
#剑指33:二叉搜索树的后序遍历

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if not sequence or length <= 0:
            return False
        root = sequence[length-1]
        j = 0
        #找到右子树的起始位置
        for i in range(length-1):
            j += 1
            if sequence[i] > root:
                break
        pre = sequence[:j]    #左子树序列
        post = sequence[j:-1] #右子树序列
        #如果右子树序列中有比根节点小的，返回False
        for val in post:
            if val < root:
                return False
        left,right = True,True
        #j > 0表示存在左子树，递归验证左子树
        if j > 0:
            left = self.VerifySquenceOfBST(pre)
        #j < length-1表示存在右子树，递归验证右子树
        if j < length-1:
            right = self.VerifySquenceOfBST(post)
        return left and right

rst = Solution()
sequence = [5,7,6,9,11,10,8]
sequence1 = [7,4,6,5]
print(rst.VerifySquenceOfBST(sequence))
print(rst.VerifySquenceOfBST(sequence1))