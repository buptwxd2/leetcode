class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, outer_num in enumerate(numbers):
            if outer_num >= target // 2 + 1:
                break

            for j in range(i + 1, len(numbers)):
                if numbers[j] + outer_num == target:
                    return i + 1, j + 1

                if numbers[j] >= target:
                    break
