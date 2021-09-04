# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:58:52 2021

@author:  Evgeniya Vorontsova
LC Problem 67 Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

    1 <= a.length, b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stock = 0
        len_a = len(a)
        len_b = len(b)
        rez = ""
        i = len_a - 1
        j = len_b - 1
        
        while j >= 0 or i >= 0:
            if i >= 0:
                cur_ai = int(a[i])
            else:
                cur_ai = 0
            
            if j >= 0:
                cur_bj = int(b[j])
            else:
                cur_bj = 0
            
            cur_sum = cur_ai + cur_bj + stock
            if cur_sum < 2:
                cur_bit = cur_ai + cur_bj + stock
                stock = 0
            elif cur_sum == 2:
                cur_bit = 0
                stock = 1
            elif cur_sum == 3:  
                cur_bit = 1
                stock = 1
                
            rez = str(cur_bit) + rez
            
            #print(i, cur_ai, cur_bj, cur_bit, stock, rez)
            i = i - 1
            j = j - 1
            
        if stock == 1:
            rez = "1" + rez          
            
        return rez
        
# Tests
a = "1010"
b = "1011"
class_instance = Solution()
rez = Solution.addBinary(class_instance, a, b)   
print(rez)            
