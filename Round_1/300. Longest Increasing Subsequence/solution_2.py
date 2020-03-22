class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis_list = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if lis_list[j] + 1 > lis_list[i]:
                        lis_list[i] = lis_list[j] + 1

        return max(lis_list)


"""
Results:
Runtime: 1572 ms, faster than 12.19% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 13.1 MB, less than 97.44% of Python3 online submissions for Longest Increasing Subsequence.
"""