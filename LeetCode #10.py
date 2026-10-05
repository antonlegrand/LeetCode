class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def matching(i: int, j: int) -> bool:
            key = (i, j)
            if key in memo:
                return memo[key]

            if j == len(p):
                result = i == len(s)
            elif j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    matching(i, j + 2)
                    or (i < len(s) and (s[i] == p[j] or p[j] == '.') and matching(i + 1, j))
                )
            else:
                result = i < len(s) and (s[i] == p[j] or p[j] == '.') and matching(i + 1, j + 1)

            memo[key] = result
            return result

        return matching(0, 0)

print(Solution().isMatch(s = "aa", p = "a"))      # False
print(Solution().isMatch("aa", "a*"))     # True
print(Solution().isMatch("ab", ".*"))     # True
print(Solution().isMatch("aab", "c*a*b"))  # True
print(Solution().isMatch("ab", ".*c"))    # False
