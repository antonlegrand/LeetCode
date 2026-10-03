"""
Exercice 5
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start = 0
        max_len = 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    start = left
                    max_len = current_len
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)      # odd-length palindromes
            expand(i, i + 1)  # even-length palindromes

        return s[start:start + max_len]

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [""] * numRows
        current_row = 0
        step = 1

        for ch in s:
            rows[current_row] += ch

            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1

            current_row += step

        return "".join(rows)
print(Solution().longestPalindrome(s = "babad"))