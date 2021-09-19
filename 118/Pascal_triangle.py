# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 23:03:13 2021

@author: Evgeniya Vorontsova

LC Problem 118 Pascal's triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers 
directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        l_cur = [1]
        rez = []
        rez.append(l_cur)
       
        for i in range(1, numRows):
            l_prev = rez[-1] 
            l_cur = [1]                   
            for j, elem in enumerate(l_prev):
                if j == 0:
                    prev = 1
                    continue
                
                l_cur.append(prev + elem)
                prev = elem    
            l_cur.append(1)        
            rez.append(l_cur)        
        return rez
           
class_instance = Solution()
rez = Solution.generate(class_instance, 20)
print(rez)             
