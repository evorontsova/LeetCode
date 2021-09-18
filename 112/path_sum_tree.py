# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:27:01 2021

@author: Evgeniya Vorontsova

LC Problem 112 Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:

Input: root = [1,2], targetSum = 0
Output: false

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        val = root.val
        right = root.right
        left = root.left
        if val == targetSum and not right and not left:
            return True
        
        right_attempt = self.hasPathSum(root.right, targetSum - val)
        
        if right_attempt:
            return True
        
        left_attempt = self.hasPathSum(root.left, targetSum - val)

        if left_attempt:
            return True
        
        return False
# Tests    
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.right = b
b.right = c
c.right = d
d.right = e
e.right = f

class_instance = Solution()
rez = Solution.hasPathSum(class_instance, a, 21)
print(rez)                
    
