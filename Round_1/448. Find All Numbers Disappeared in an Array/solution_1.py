class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_set = set(range(1, 1 + len(nums)))

        return list(my_set - set(nums))
