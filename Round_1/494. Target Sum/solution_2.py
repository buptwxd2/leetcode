class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0

        dp = [{} for _ in range(len(nums))]

        # initialize
        dp[0][nums[0]] = 1
        curr_num = dp[0].setdefault(-1 * nums[0], 0)
        curr_num += 1
        dp[0][-1 * nums[0]] = curr_num

        for i in range(1, len(nums)):
            for num, times in dp[i - 1].items():
                key = num + nums[i]
                curr_times = dp[i].setdefault(key, 0)
                curr_times += times
                dp[i][key] = curr_times

                key = num - nums[i]
                curr_times = dp[i].setdefault(key, 0)
                curr_times += times
                dp[i][key] = curr_times

        return dp[-1][S] if S in dp[-1] else 0


"""
Results:
Use DP way
Runtime: 244 ms, faster than 73.78% of Python3 online submissions for Target Sum.
Memory Usage: 14.1 MB, less than 61.78% of Python3 online submissions for Target Sum.
"""