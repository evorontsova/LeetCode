# -*- coding: utf-8 -*-
"""
LC Problem 14 Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

from typing import List

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:

        num_str = len(strs)
        if num_str == 1:
            return strs[0]
        
        min_len = min([len(st) for st in strs])
        if min_len == 0:
            return ""
        
        rez_old = strs[0]
        for ii in range(1, num_str):
            j = 0
            rez = "" 
            while rez_old[j] == strs[ii][j]:
                rez = rez + strs[0][j]
                j = j + 1
                
                if j > min_len - 1:
                    break
            rez_old = rez
            len_new = len(rez_old)
            if len_new < min_len:
                min_len = len_new
            if j == 0:
                break
        return rez

 
# Tests
class_instance = Solution()
print(Solution.longestCommonPrefix(class_instance, ["acc","aaa","aaba"])) 
print(Solution.longestCommonPrefix(class_instance, ["d", "do","dog","d"]))            
print(Solution.longestCommonPrefix(class_instance, ["a"]))    
print(Solution.longestCommonPrefix(class_instance, ["reflower","flow","flight"]))       
print(Solution.longestCommonPrefix(class_instance, ["flower","flower2","flight"]))     
