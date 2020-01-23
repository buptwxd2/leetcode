class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index_dict = {}

        for index, num in enumerate(nums):
            if num in value_index_dict and (index - value_index_dict[num]) <= k:
                return True

            value_index_dict[num] = index

        return False
