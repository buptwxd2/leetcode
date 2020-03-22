# try back

class Solution:
    def lengthOfLIS(self, nums) -> int:
        max_lis = 0

        if not nums:
            return max_lis

        def lis(i, current_lis):
            nonlocal max_lis

            if i == len(nums):
                if len(current_lis) > max_lis:
                    max_lis = len(current_lis)

                return

            # NOT add the i-th element
            lis(i + 1, current_lis)

            # Add the i-th element
            if not current_lis:
                lis(i + 1, [nums[i]])
            else:
                if nums[i] <= current_lis[-1]:
                    return
                new_list = current_lis.copy()
                new_list.append(nums[i])
                lis(i + 1, new_list)

        lis(0, [])

        return max_lis

s = Solution()
print(s.lengthOfLIS([2, 2]))


"""
Results:
Time Limit Exceeded
"""
