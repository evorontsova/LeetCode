# -*- coding: utf-8 -*-
"""
Created on Sat Sep 4 22:32:42 2021

@author: Evgeniya Vorontsova
LC Problem 69 Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, 
the decimal digits are truncated, and only 
the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or
 operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # It is a brute-force solution, not effective
        # fancy Newton
        if x == 1:
            return 1
        
        half = x // 2 + 1
        
        cur_sq = 1
        cur_sqrt = 1
        for i in range(1, half+1):
            if cur_sq > x:
                return cur_sqrt-1
            elif cur_sq == x:
                return cur_sqrt
            else:
                cur_sq = cur_sq + 2 * i + 1
                cur_sqrt = cur_sqrt + 1
    
# Tests
x = 100
class_instance = Solution()
rez = Solution.mySqrt(class_instance, x)   
print(rez)        
