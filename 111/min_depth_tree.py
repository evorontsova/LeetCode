# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:59:01 2021

@author: Evgeniya Vorontsova

LC Problem 111 Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
    The number of nodes in the tree is in the range [0, 105].
    -1000 <= Node.val <= 1000
"""
from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = root.left
        right = root.right
                
        if not left and not right:
            return 1
        
        if right:
            path_r = self.minDepth(right)
        else:
            path_r = 1e6 # This number is more than any minDepth (by conditions)
            
        if left:
            path_l = self.minDepth(left)
        else:
            path_l = 1e6
            
        return 1 + min(path_r, path_l)
        
# Tests    
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(17)
e = TreeNode(35)
f = TreeNode(7)
a.right = b
b.right = c
c.right = d
e.right = f

class_instance = Solution()
rez = Solution.minDepth(class_instance, a)
print(rez)                
    
