# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:48:29 2021

@author: Evgeniya Vorontsova

LC Problem 53 Maximum Subarray

Given an integer array nums, 
find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

    1 <= nums.length <= 3 * 10^4
    -10^5 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, 
which is more subtle.
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic programming approach
        max_sum = nums[0]
        len_arr = len(nums)
        dp = [max_sum]
        
        for i in range(1, len_arr):
            cur_elem = nums[i]
            dp_i = max(dp[i-1] + cur_elem, cur_elem)
            dp.append(dp_i)
            if dp_i > max_sum:
                max_sum = dp_i
        
        #print(dp)    
        return max_sum

    
# Tests
nums = [5, 4, -1, 7, 8]
class_instance = Solution()
rez = Solution.maxSubArray(class_instance, nums)   
print(rez)                
