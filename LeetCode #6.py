class Solution:
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

print(Solution().convert(s = "PAYPALISHIRING", numRows = 4))