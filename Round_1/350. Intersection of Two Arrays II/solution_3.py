class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        result = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result

"""
Results:
双指针方法
Runtime: 56 ms, faster than 43.98% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14 MB, less than 47.88% of Python3 online submissions for Intersection of Two Arrays II.
"""