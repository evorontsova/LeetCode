# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:15:15 2021

@author: Evgeniya Vorontsova

LC Problem 58 Length of Last Word

Given a string s consisting of some words 
separated by some number of spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        len_s = len(s)
        i = len_s - 1
        last_word = 0
        while s[i] != " " and i >= 0:
            last_word = last_word + 1
            i = i - 1
        return last_word

# Tests
s = "   fly me   to   the moon  "
class_instance = Solution()
rez = Solution.lengthOfLastWord(class_instance, s)   
print(rez)                    
