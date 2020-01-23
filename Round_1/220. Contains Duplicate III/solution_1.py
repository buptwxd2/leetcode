## Not Accepted due to "Time Limit Exceeded"

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) == 0 or len(nums) == 1:
            return False

        index = 0
        for index in range(len(nums)):
            sub_nums = nums[index: index + k + 1]
            if self.containsAlmostDuplicate(sub_nums, t):
                return True

        return False

    def containsAlmostDuplicate(self, nums, t):
        current_num = nums[0]

        for num in nums[1:]:
            if abs(current_num - num) <= t:
                return True

        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([-5,5,5,5,5,15], 6, 6))
