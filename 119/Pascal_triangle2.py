# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 23:40:32 2021

@author: Evgeniya Vorontsova

LC Problem 119 Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of 
the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers 
directly above it

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
    0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        l_cur = [1]
        triangle = []
        triangle.append(l_cur)
       
        for i in range(1, rowIndex+1):
            l_prev = triangle.pop()
            l_cur = [1]                   
            for j, elem in enumerate(l_prev):
                if j == 0:
                    prev = 1
                    continue
                
                l_cur.append(prev + elem)
                prev = elem    
            l_cur.append(1)        
            triangle.append(l_cur)        
        return triangle.pop()       
        
class_instance = Solution()
rez = Solution.getRow(class_instance, 3)
print(rez)                     
