class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        n = len(s)

# first condition : whitespace 
        while i < n and s[i] == " ":
            i += 1

# second condition : determine the sign of the string 
        sign = 1
        if i < n and s[i] in ("+", "-"):
            if s[i] == "-":
                sign = -1
            i += 1

# third condition : skip leading zero until no digit caracter 
        result = 0
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

#fourth condition : if out of the borne , round the integer 
            limit = 2**31 if sign == -1 else 2**31-1

            if result > limit // 10 or (result == limit // 10 and digit > limit % 10):
                return -2**31 if sign == -1 else 2**31-1

            result = result * 10 + digit
            i += 1

        return sign * result
print(Solution().myAtoi(s = "42"))
print(Solution().myAtoi(s = "-042"))
print(Solution().myAtoi(s = "1337c0d3"))
print(Solution().myAtoi(s = "0-1"))
print(Solution().myAtoi(s = "words and 987"))
