# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:09:38 2021

LC Problem 100 Same Tree

Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.

Two binary trees are considered the same 
if they are structurally identical, and 
the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false 

Constraints:
    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4
"""

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
         
class Solution:
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # The idea of the algorithm is from here:
        # https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python  
        
        if p and q:
           flag_val = p.val == q.val
           flag_left = self.isSameTree(p.left, q.left)         
           flag_right = self.isSameTree(p.right, q.right)
            
           return flag_val and flag_left and flag_right
        
        # Operator is checks if two operands refer to the same object in memory,
        # so, in that case we check if both p and q is None, because the other cases 
        # we analyzed above  
        return p is q


# Tests
a = TreeNode(5)
b = TreeNode(6)
c = TreeNode(8)
d = TreeNode(9)
e = TreeNode(35)
f = TreeNode(7)
a.right = f
a.left = b
b.left = c
b.right = d
f.left = e


class_instance = Solution()
rez = Solution.isSameTree(class_instance, a, b)
print(rez)         
