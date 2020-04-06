class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_1, len_2 = len(num1), len(num2)

        i, j = len_1 - 1, len_2 - 1
        carry_bit = 0

        sum_list = []

        while i >= 0 and j >= 0:
            current_sum = int(num1[i]) + int(num2[j]) + carry_bit
            sum_list.append(current_sum % 10)

            carry_bit = current_sum // 10

            i -= 1
            j -= 1

        while i >= 0:
            current_sum = int(num1[i]) + carry_bit
            sum_list.append(current_sum % 10)
            carry_bit = current_sum // 10

            i -= 1

        while j >= 0:
            current_sum = int(num2[j]) + carry_bit
            sum_list.append(current_sum % 10)
            carry_bit = current_sum // 10

            j -= 1

        if carry_bit != 0:
            sum_list.append(carry_bit)

        return "".join(str(i) for i in sum_list[::-1])

"""
Results:
Runtime: 80 ms, faster than 11.98% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Add Strings.
"""