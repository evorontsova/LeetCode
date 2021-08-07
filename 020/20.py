# -*- coding: utf-8 -*-
"""
LC Problem 20 Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true


Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:

        len_s = len(s)
        if len_s%2 == 1:
            return False
        
        stack = []
        
        list_open = ['(', '{', '[']
        for i in s:
            if i in list_open:
                stack.append(i)
            else:
                # In that case we have a bracket of closed type
                
                if stack:
                    last_b = stack.pop()
                
                    if last_b not in list_open:
                        return False
                
                    if last_b + i not in ["()", "[]", "{}"]:
                        return False
                else:
                    return False

        if not stack:
            # Our stack is empty, it's ok!
            return True
          
        return False


# Test
class_instance = Solution()
print(Solution.isValid(class_instance, "([][][][][])"))            
