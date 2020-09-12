class Solution:
    def getPermutation(self, n, k):
        nums, result = [i + 1 for i in range(n)], ''

        while n > 0:
            totalCount = math.factorial(n - 1)
            index = (k - 1) / totalCount
            result += str(nums.pop(index))
            n -= 1
            k %= totalCount

        return result