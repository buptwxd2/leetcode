class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) == 0 or len(A) == 1:
            return [x ** 2 for x in A]

        left = 0
        right = len(A) - 1

        tmp = []

        while left <= right:
            if A[left] ** 2 <= A[right] ** 2:
                tmp.append(A[right] ** 2)
                right -= 1
            else:
                tmp.append(A[left] ** 2)
                left += 1

        return reversed(tmp)

"""
Results:
Runtime: 316 ms, faster than 11.32% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.4 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
"""