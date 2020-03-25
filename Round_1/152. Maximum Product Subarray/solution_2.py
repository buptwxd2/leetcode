class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max_positive = global_max_negative = nums[0]
        current_max_positive = current_max_negative = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                current_max_positive = max(nums[i], nums[i] * current_max_positive)
                current_max_negative = min(nums[i], nums[i] * current_max_negative)
            else:
                tmp_positive = current_max_positive
                current_max_positive = max(nums[i], nums[i] * current_max_negative)
                current_max_negative = min(nums[i], nums[i] * tmp_positive)

            if current_max_positive > global_max_positive:
                global_max_positive = current_max_positive
            if current_max_negative < global_max_negative:
                global_max_negative = current_max_negative

        return global_max_positive