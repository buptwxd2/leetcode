class Solution:
    def titleToNumber(self, s: str) -> int:
        my_dict = {chr(i + ord('A')): i + 1 for i in range(26)}

        if not s:
            return 0

        output = my_dict[s[0]]

        for char in s[1:]:
            output = output * 26
            char_int = my_dict[char]

            output += char_int

        return output

"""
Results:
Runtime: 24 ms, faster than 95.98% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 14.1 MB, less than 5.44% of Python3 online submissions for Excel Sheet Column Number.
"""