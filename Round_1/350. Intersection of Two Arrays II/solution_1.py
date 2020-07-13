class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1_dict = {}

        result_dict = {}

        for num in nums1:
            cnt = nums1_dict.setdefault(num, 0)
            cnt += 1
            nums1_dict[num] = cnt

        for num in nums1_dict.keys():
            common_cnt = min(nums1_dict[num], nums2.count(num))
            if common_cnt > 0:
                result_dict[num] = common_cnt

        results = []

        for num in result_dict:
            for _ in range(result_dict[num]):
                results.append(num)

        return results