# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:57:43 2021

@author: Evgeniya Vorontsova

LC Problem 94 Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [1,2]

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    
    # Recursive version
    
    def rec_trav(self, node: Optional[TreeNode], inord_list: List[int]):
        left = node.left
        if left:
            self.rec_trav(left, inord_list)
            
        if node:
            inord_list.append(node.val)
        
        right = node.right    
        
        if right:
            self.rec_trav(right, inord_list)
        
        return inord_list
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
               
        if not root:
            return []
        
        inord_list = []
        
        inord_list = self.rec_trav(root, inord_list)
        
        return inord_list
    
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
rez = Solution.inorderTraversal(class_instance, a)
print("Tree InOrder Traversal:")
if rez:
    print(rez) 
                
