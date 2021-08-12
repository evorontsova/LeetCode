# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 2021

@author: Evgeniya Vorontsova

LC Problem 28 Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:

Input: haystack = "", needle = ""
Output: 0

Constraints:

    0 <= haystack.length, needle.length <= 5 * 104
    haystack and needle consist of only lower-case English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if haystack == "":
            return -1
        
        rez = -1
        len_needle = len(needle)
        len_haystack = len(haystack)
        
        for i in range(0, len_haystack):
            if haystack[i: min([i + len_needle, len_haystack])] == needle:
                rez = i
                break
        return rez
            
# Tests
s1 = "wwwwfaf3"
s2 = "faf"
class_instance = Solution()
rez = Solution.strStr(class_instance, s1, s2)   
print(rez)         
    
