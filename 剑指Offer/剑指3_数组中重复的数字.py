# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:34:46 2019

@author: WinJX
"""

#剑指3 : 数组中重复的数字
"""
                    题目1
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是重复的数字2或3。
"""
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    
    #判断数字是否在0到n-1之间
    def judge(self,numbers):
        length = len(numbers)
        for num in numbers:
            if num >=length or num < 0:
                return False
        return True
     
    #法一，扫描
    def duplicate1(self, numbers, duplication):
        if not numbers or not self.judge(numbers):
            return False
        for num in numbers:
            if numbers.count(num) > 1:
                duplication[0] = num
                return True
        return False
    
    #法二：哈希判断
    def duplicate2(self, numbers, duplication):
        if not numbers or not self.judge(numbers):
            return False
        hash_set = set()
        for num in numbers:
            if num not in hash_set:
                hash_set.add(num)
            else:
                duplication[0] = num
                return True
        return False
    
    #法三 ：比较交换
    def duplicate3(self, numbers, duplication):
        if not numbers or not self.judge(numbers):
            return False
        idx = 0
        while idx < len(numbers):
            #获得当前数字m
            tmp = numbers[idx]
            #判断是否等于idx，如果是则扫描下一个数字
            if tmp == idx:
                idx += 1
            #否则与第idx个数字比较，若相等，则重复
            elif tmp == numbers[tmp]:
                duplication[0] = tmp
                return True
            #否则交换数字继续比较
            else:
                numbers[idx],numbers[tmp] = numbers[tmp],numbers[idx]
        return False
    
    #法四：collections大法
    def duplicate4(self, numbers, duplication):
         from collections import Counter
         if not numbers or not self.judge(numbers):
            return False
         cnt = Counter(numbers)
         most_one = cnt.most_common(1)   #获取出现次数最多的数字和频数
         if most_one[0][1] > 1:           
             duplication[0] = most_one[0][0]
             return True
         return False
                
    
    
rst = Solution()
#测试用例
numbers0 = [2,3,1,0,2,5,3] #正常
numbers1 = []              #空的情况
numbers2 = [-1,2,2,4,5,8]  #数字-1和8不符合要求
numbers3 = [0,1,2,3,4]     #无重复数字测试
print(rst.duplicate1(numbers0,[0]))
print(rst.duplicate2(numbers1,[0]))
print(rst.duplicate3(numbers2,[0]))
print(rst.duplicate4(numbers3,[0]))


"""
                    题目2
            不修改数组找出重复的数字
在一个长度为n+1的数组里的所有数字都在1到n的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,5,4,3,2,6,7}，
那么对应的输出是重复的数字2或3。
"""
class Solution1:
    #辅助空间
    def getDuplication1(self,numbers):
        if not numbers or not self.judge(numbers):
            return False
        lst = [0]*len(numbers)
        for num in numbers:
            if lst[num]:
                return num
            else:
                lst[num] = num
        return False
    
    #类似二分查找思路
    def getDuplication2(self,numbers):
        if not numbers or not self.judge(numbers):
            return False
        length = len(numbers)
        start,end = 1,length - 1
        while start <= end:
            mid = (start+end)//2
            count = self.countRange(numbers,length,start,mid)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return False
    
    #判断数字是否在1到n之间
    def judge(self,numbers):
        length = len(numbers)
        for num in numbers:
            if num > length or num < 1:
                return False
        return True
    
    #计数
    def countRange(self,numbers,length,start,end):
        if not numbers:
            return 0
        count = 0
        for i in range(length):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1
        return count
        
        
ret = Solution1()
numbers = [2,3,5,4,3,2,6,7]
numbers4 = [0,1,2,3,4,2]
numbers5 = []
numbers6 = [1,2,3,4,5,6]
print(ret.getDuplication1(numbers))
print(ret.getDuplication2(numbers4))
print(ret.getDuplication1(numbers5))
print(ret.getDuplication2(numbers6))    
    


