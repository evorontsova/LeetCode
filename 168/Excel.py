# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:36:29 2021

@author: Evgeniya Vorontsova

LC Problem 168  Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"

Constraints:
    1 <= columnNumber <= 2^31 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # Let's translate the number to 26-digits number
        # system. One little problem: it's not a real
        # 26-digits system, because this is no 0.
        # So, we need to substract 1 in that case
        ost = columnNumber
        if ost == 1:
            return 'A'
        rez = ''
        
        l = []
        base = 26 
        while ost > 0:
            digit = ost % base
            ost = ost // base
            
            if digit == 0:
                l.append('Z')
                ost = ost - 1    
            
            else:
                l.append(chr(digit + 64))
                
            #print(digit, ost, l)
        
        for i in l[::-1]:
            rez = rez + i
        return rez

        

class_instance = Solution()
rez = Solution.convertToTitle(class_instance, 51)
print(rez)      
