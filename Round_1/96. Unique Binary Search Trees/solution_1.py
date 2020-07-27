class Solution:
    def numTrees(self, n: int) -> int:
        memory = [-1] * (n + 1)

        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2

        memory[0] = memory[1] = 1
        memory[2] = 2

        for i in range(3, n + 1):
            tmp = 0

            for j in range(i):
                tmp += memory[j] * memory[i - j - 1]

            memory[i] = tmp

        return memory[-1]


"""
Results:
Runtime: 36 ms, faster than 19.18% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 13.9 MB, less than 32.59% of Python3 online submissions for Unique Binary Search Trees.
"""