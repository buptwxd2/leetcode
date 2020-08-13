class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) == 0 or int(num2) == 0:
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        m, n = len(num1), len(num2)

        results = []

        carry_out = 0
        for i in range(0, m + n - 1):

            tmp = 0
            for j in range(0, min(i + 1, m)):
                k = i - j
                if k > n - 1:
                    continue

                tmp += int(num1[j]) * int(num2[k])

            tmp += carry_out
            results.append(tmp % 10)
            carry_out = tmp // 10

        if carry_out:
            results.append(carry_out)

        return "".join(str(x) for x in results[::-1])

"""
Results:
Runtime: 116 ms, faster than 48.87% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.6 MB, less than 95.49% of Python3 online submissions for Multiply Strings.
"""