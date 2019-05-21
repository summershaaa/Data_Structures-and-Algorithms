# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:30:46 2019

@author: WinJX
"""

#剑指17：打印从1到最大的n位数

class Solution:
    def print_to_max_N_digits(self,n):
        if n <= 0:
            return

        digits = [0] * n
        self.print_digits_recursivly(digits, len(digits), 0)


    def print_digits_recursivly(self,digits, length, index):
        if index == length:
            self.print_digits(digits)
            return

        for i in range(0, 10):
            digits[index] = str(i)
            self.print_digits_recursivly(digits, length, index + 1)


    def print_digits(self,digits):
        is_begin_with_zero = True
        result = ''
        for num in digits:
            if is_begin_with_zero and num != '0':
                is_begin_with_zero = False
            if not is_begin_with_zero:
                result += num
        if result != '':
            print(result)
    
rst = Solution()
rst.print_to_max_N_digits(2)
