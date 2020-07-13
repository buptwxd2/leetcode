class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

"""
Results:
Runtime: 60 ms, faster than 36.37% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 13.9 MB, less than 78.12% of Python3 online submissions for Intersection of Two Arrays.
"""