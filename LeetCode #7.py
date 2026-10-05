"""
Exercice 7

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = -1 if x < 0 else 1
        num = abs(x)
        result = 0
        limit = 2**31 if x < 0 else 2**31 - 1

        while num > 0:
            digit = num % 10
            result = result * 10 + digit
            num //= 10

        if result > limit:
            return 0

        return sign * result