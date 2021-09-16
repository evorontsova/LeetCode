# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:18:38 2021

@author: Evgeniya Vorontsova

LC Problem 110 Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in 
    height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
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
    # Recursive function to find a maximum depth of the binary tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # We add +1, because we need to count root as one node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
          
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if abs(self.maxDepth(root.right) - self.maxDepth(root.left)) > 1:
            return False
        
        rez_left = self.isBalanced(root.left)
        
        if not rez_left:
            return False
        
        rez_right = self.isBalanced(root.right)
        
        if not rez_right:
            return False
        
        return True
        
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
rez = Solution.isBalanced(class_instance, a)
print(rez)             
