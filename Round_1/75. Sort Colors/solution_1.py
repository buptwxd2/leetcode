class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cnts = [0, 0, 0]  # red, white, bule

        for num in nums:
            if num == 0:
                cnts[0] += 1
            elif num == 1:
                cnts[1] += 1
            else:
                cnts[2] += 1

        # write 0
        offset = 0
        for i in range(cnts[0]):
            nums[i] = 0

        # write 1
        offset = cnts[0]
        for i in range(cnts[1]):
            nums[i + offset] = 1

        # write 2
        offset += cnts[1]
        for i in range(cnts[2]):
            nums[i + offset] = 2

        return

"""
Results:
Runtime: 16 ms, faster than 99.99% of Python3 online submissions for Sort Colors.
Memory Usage: 14.3 MB, less than 5.09% of Python3 online submissions for Sort Colors.
"""