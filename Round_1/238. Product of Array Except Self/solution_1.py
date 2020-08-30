class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)

        left_products = [1] * m
        right_products = [1] * m

        for i in range(1, m):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        for j in range(m - 2, -1, -1):
            right_products[j] = right_products[j + 1] * nums[j + 1]

        results = [left_products[i] * right_products[i] for i in range(m)]

        return results

"""
Results:
Runtime: 128 ms, faster than 72.84% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.9 MB, less than 19.58% of Python3 online submissions for Product of Array Except Self.
"""