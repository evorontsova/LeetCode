# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:59:46 2021

@author: Evgeniya Vorontsova

LC Problem 125 Valid Palindrome
Given a string s, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""
import string

class Solution:
    # Two-pointers approach
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        if len_s == 1:
            return True

        p_first = 0
        p_last = len_s - 1
        
        while p_first < p_last:
            s_i = s[p_first]
            while not s_i.isalnum() and p_first < p_last:
                p_first = p_first + 1
                s_i = s[p_first]
            
            s_j = s[p_last] 
            while not s_j.isalnum() and p_last > p_first:
                p_last = p_last - 1
                s_j = s[p_last]    
            
            if s_i.lower() != s_j.lower():
                return False
            
            p_first = p_first + 1
            p_last = p_last - 1
            
        return True    
        
s = "A man, a plan, a canal: Panama"
class_instance = Solution()
rez = Solution.isPalindrome(class_instance, s)
print(rez)                      
