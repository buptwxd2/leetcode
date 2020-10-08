class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        length = len(A)

        if length == 0 or length == 1:
            return A

        left, right = 0, length - 1

        def swap(A, i, j):
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

        while left < right:
            while left < right and A[left] % 2 == 0:
                left += 1

            while right > left and A[right] % 2 != 0:
                right -= 1

            swap(A, left, right)
            left += 1
            right -= 1

        return A

"""
Results:
Runtime: 80 ms, faster than 84.46% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.6 MB, less than 11.73% of Python3 online submissions for Sort Array By Parity.
"""