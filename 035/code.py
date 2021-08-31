# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 2021

@author: Evgeniya Vorontsova


LC Problem 35 Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0

Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        
        left = 0
        right = len_nums - 1
        prev_len = len_nums
        
        while True:
            
            half = left + (right - left) // 2
            
            #print(half, left, right)
            val_half = nums[half]
            
            if target > val_half:
                left = half
            elif target < val_half:
                right = half
            else:
                return half
           
            if left == right:
                break
            
            val_right = nums[right]

            if right - left == 1 and prev_len == 1:
                if target > val_right:
                    return right + 1
                else:
                    return right
            else:
                prev_len = right - left
          
        if target > val_half:
            return half + 1
        else:
            return half
# Tests
nums = [1]
target = 0
class_instance = Solution()
rez = Solution.searchInsert(class_instance, nums, target)   
print(rez)         
    
