# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:39:20 2019

@author: WinJX
"""

#剑指56：数组中数字出现的次数

class Solution:
    #题目一：数组中只出现一次的两个数字
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
#        from collections import Counter
#        rst = []
#        cnt = Counter(array)
#        for k,v in cnt.items():
#            if v == 1:
#                rst.append(k)
#        return rst
        
        if len(array)<2:
            return []
        temp = 0
        for val in array:
            temp ^= val
        #获取temp二进制中最右边1的下标
        index = 0
        while temp !=0 and temp&1==0:
            index += 1
            temp = temp>>1
        #获取index对应的值
        num = 1<<index
        result = [0,0]
        for val in array:
            if num&val:
                result[0] ^= val
            else:
                result[1] ^= val
        return result
        
    #题目2：数组中唯一只出现一次的数字
    #只有一次出现一次，其他数字都出现三次
    def FindNumberAppearingOnce(self,array):
        #出现负数
        if any([x<0 for x in array]):
            return []
        length = len(format(max(array),'b'))
        result = [0]*length
        for val in array:
            bin_val = format(val,'b')[::-1]
            #统计数字二进制中1出现的次数
            for i in range(len(bin_val)):
                if int(bin_val[i]):
                    result[i] += 1
        #若对应位置1出现的次数能被3整除，则出现一次的数字二进制中对应位置为0.
        result = [x%3 for x in result[::-1]]
        return int(''.join([str(x) for x in result]),2)
            
        
        
        
        
    
rst = Solution()
print(rst.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))
print(rst.FindNumberAppearingOnce([-3,3,3,3,5,5,5,7,7,7]))