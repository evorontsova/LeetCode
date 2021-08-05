# -*- coding: utf-8 -*-
"""
LC Problem 13 Roman to Integer

Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        len_s = len(s)
        int_num = 0
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,  
                           'D': 500, 'M': 1000}
        while (len_s > 0):
            if (len_s > 1):
                if s[0] == 'I' and s[1] == 'V':
                    int_num = int_num + 4
                    s = s[2:]
                elif s[0] == 'I' and s[1] == 'X':
                    int_num = int_num + 9
                    s = s[2:] 
                elif s[0] == 'X' and s[1] == 'L':
                    int_num = int_num + 40
                    s = s[2:]    
                elif s[0] == 'X' and s[1] == 'C':
                    int_num = int_num + 90
                    s = s[2:]
                elif s[0] == 'C' and s[1] == 'D':
                    int_num = int_num + 400
                    s = s[2:]    
                elif s[0] == 'C' and s[1] == 'M':
                    int_num = int_num + 900
                    s = s[2:]  
                else:
                    int_num = int_num + dict_roman[s[0]]
                    s = s[1:]
            else:
                return int_num + dict_roman[s[0]]
            len_s = len(s)
            
        return int_num

# Test
print(Solution.romanToInt("", "LXVIII"))    
