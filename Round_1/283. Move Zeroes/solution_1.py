class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_count = nums.count(0)
        for i in range(zero_count):
            nums.remove(0)

        nums.extend([0] * zero_count)

        return None
