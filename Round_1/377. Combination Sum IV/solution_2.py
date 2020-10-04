class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = {}

        def recur_dp(nums, target, dp):
            if target in dp:
                return dp[target]

            count = 0
            for num in nums:
                if num <= target:
                    new_target = target - num
                    if new_target == 0:
                        count += 1
                        continue

                    count += recur_dp(nums, new_target, dp)

            dp[target] = count

            return count

        count = recur_dp(nums, target, dp)

        return count

"""
"""