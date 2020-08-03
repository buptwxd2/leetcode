class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return num1 or num2

        i, j = len(num1) - 1, len(num2) - 1
        carry_bit = 0
        result = []

        while i >= 0 and j >= 0:
            tmp = int(num1[i]) + int(num2[j]) + carry_bit
            carry_bit = tmp // 10
            remainder = tmp % 10

            result.append(remainder)

            i -= 1
            j -= 1

        if i >= 0:
            remaining_idx = i
            remaining_num = num1
        elif j >= 0:
            remaining_idx = j
            remaining_num = num2
        else:
            remaining_idx = -1

        if remaining_idx >= 0:

            while remaining_idx >= 0:
                tmp = int(remaining_num[remaining_idx]) + carry_bit
                carry_bit = tmp // 10
                remainder = tmp % 10

                result.append(remainder)

                remaining_idx -= 1

        if carry_bit:
            result.append(carry_bit)

        result.reverse()

        return ''.join([str(num) for num in result])

"""
Results:
Runtime: 40 ms, faster than 84.31% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 60.13% of Python3 online submissions for Add Strings.
"""