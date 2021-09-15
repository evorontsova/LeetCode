# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:07:26 2021

@author: Evgeniya Vorontsova

LC Problem 108 Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.
"""

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        len_nums = len(nums)
        
        half = (len_nums-1) // 2
        
        root = TreeNode(nums[half])
        
        if half-1 >= 0:
            left_list = nums[:half]
            root.left = self.sortedArrayToBST(left_list)
        
        if len_nums - half - 1 > 0:
            right_list = nums[half+1:]
            root.right = self.sortedArrayToBST(right_list)
        
        return root    

# Tests    
nums = [3, 5, 8] 
class_instance = Solution()
rez = Solution.sortedArrayToBST(class_instance, nums)
print(rez.val, rez.left.val, rez.right.val)         
   
