"""
Exercice 14 

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
si la première lettre de mot 1 = mot 2 = mot 3 alors prefix = lettre1
bloucle suivante 
lettre 2 
sinon stop 
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# Tests
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["car", "care", "carmin"]))