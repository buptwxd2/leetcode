class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp_list = []
        i, j = m - 1, n - 1
        anchor = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[anchor] = nums1[i]
                i -= 1
            else:
                nums1[anchor] = nums2[j]
                j -= 1

            anchor -= 1

        if i < 0:
            nums1[0:anchor + 1] = nums2[0:j + 1]
        else:
            nums1[0:anchor + 1] = nums1[0:i + 1]

        return


"""
Results:
Runtime: 32 ms, faster than 83.81% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""