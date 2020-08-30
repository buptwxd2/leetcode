class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)

        results = left_products = [1] * m

        for i in range(1, m):
            results[i] = results[i - 1] * nums[i - 1]

        R = 1
        for j in range(m - 1, -1, -1):
            results[j] = results[j] * R
            R = R * nums[j]

        return results

"""
Results:
O(1) space
Runtime: 124 ms, faster than 83.96% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.4 MB, less than 79.59% of Python3 online submissions for Product of Array Except Self.
"""