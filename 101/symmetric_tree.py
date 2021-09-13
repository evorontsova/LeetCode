# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:42:47 2021

@author: Evgeniya Vorontsova

LC Problem 101 Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
         
class Solution:
    # Recursive version, we need to check if the left subtree of node1 is 
    #a reflection of the right subtree of node2
    def isMirror(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        
        return node1.val == node2.val and \
            self.isMirror(node1.left, node2.right) and \
            self.isMirror(node1.right, node2.left)                                             
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
         
        return self.isMirror(root.left, root.right)
  
# Tests
a = TreeNode(1)
b1 = TreeNode(2)
b2 = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
a.right = b1
a.left = b2
b1.left = c
b1.right = d
b2.left = d
b2.right = c


class_instance = Solution()
rez = Solution.isSymmetric(class_instance, a)
print(rez)         
