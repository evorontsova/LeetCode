# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:02:37 2021

@author: Evgeniya Vorontsova

LC Problem 104 Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -100 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
         
class Solution:
    # Recursive version
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            # We add +1, because we need to count root as one node
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
          
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
rez = Solution.maxDepth(class_instance, a)
print(rez)         
