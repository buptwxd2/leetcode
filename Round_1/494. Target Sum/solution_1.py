class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0

        length = len(nums)
        solution = 0

        def dfs(i, path):
            nonlocal solution

            if len(path) == length:
                if sum(path) == S:
                    solution += 1

                return

            path_copy = path[:]
            path_copy.append(nums[i])
            dfs(i + 1, path_copy)

            path_copy = path[:]
            path_copy.append(-1 * nums[i])
            dfs(i + 1, path_copy)

        dfs(0, [])

        return solution

s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))

"""
Time Limit Exceeded
"""