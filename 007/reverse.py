"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

"""

class Solution:
    def reverse(self, x: int) -> int:
        ax = abs(x)
        sx = str(ax)
        nd = len(sx)
        ans = ''
        for i in range(nd-1, -1, -1):
            k = sx[i]
            ans = ans + k
        if x < 0:
            ans = '-' + ans
        na = int(ans)
        if abs(na) > 2**31-1:
            na = 0
        return na    
        
