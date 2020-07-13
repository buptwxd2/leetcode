class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build a less dict using the smaller list
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)

        nums1_dict = {}

        for num in nums1:
            cnt = nums1_dict.setdefault(num, 0)
            cnt += 1
            nums1_dict[num] = cnt

        result = []
        for num in nums2:
            cnt = nums1_dict.get(num, 0)
            if cnt > 0:
                result.append(num)
                nums1_dict[num] = cnt - 1

        return result

"""
Results:
Build a less dict using the smaller list
Runtime: 48 ms, faster than 73.57% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.9 MB, less than 68.25% of Python3 online submissions for Intersection of Two Arrays II.
"""