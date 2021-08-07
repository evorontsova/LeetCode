# -*- coding: utf-8 -*-
"""
!!! It's a variation of the LC Problem 14,
when the longest prefix is not necessary common
amongst ALL the strings (as it is required in Problem 14)

Longest Common Prefix between pairs of strings


Write a function to find the longest common prefix string 
amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "flow"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from typing import List

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        cur_pref = ""
        max_len_pref = 0
        num_str = len(strs)
        for ii in range(0, num_str):
                for jj in range(ii+1, num_str):
                    cur_rez = ''.join(self.com_pref(strs[ii], strs[jj]))
                    if cur_rez != "":
                        cur_len = len(cur_rez)
                        if cur_len > max_len_pref:
                            max_len_pref = cur_len
                            cur_pref = cur_rez
        
           
        return cur_pref

    def com_pref(self, s1: str, s2: str):
        for a, b in zip(s1, s2):
            if a == b:
                yield a
            else:
                return

# Test
class_instance = Solution()
print(Solution.longestCommonPrefix(class_instance, ["dog","racecar","car"]))            
print(Solution.longestCommonPrefix(class_instance, ["a"]))    
print(Solution.longestCommonPrefix(class_instance, ["reflower","flow","flight"]))        
print(Solution.longestCommonPrefix(class_instance, ["flower","flow","flight", "ff"]))        
            