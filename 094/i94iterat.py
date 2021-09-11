# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 21:20:41 2021

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
    
    # Iterative version
    
    # We keep elements in stack, first we find the last element in the left,
    # than check if it has right child or not, and
    # than we go up by means of our stack
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
               
        if not root:
            return []
        
        inord_list = []
        
        stack = []
        
        node = root
        while True:
            while True:
                if node:
                    stack.append(node)
                    left = node.left
                               
                if left is None:
                    break
                else:
                    node = left
            
            if len(stack) != 0:
                node = stack.pop()    
                inord_list.append(node.val)
                
                node = node.right
            else:
                break
        
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
