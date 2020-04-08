class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return left + 1, right + 1

        return -1, -1

"""
Results:
Runtime: 64 ms, faster than 66.03% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.2 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.
"""