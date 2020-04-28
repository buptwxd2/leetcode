class Solution:
    def isHappy(self, n: int) -> bool:
        squares = set()

        def square_sum(digits):
            return sum(i ** 2 for i in digits)

        def get_digits(n):
            digits = []
            while n:
                digits.append(n % 10)
                n = n // 10

            return digits

        m = n
        while True:
            digits = get_digits(m)
            my_sum = square_sum(digits)

            if my_sum == 1:
                return True

            if my_sum in squares:
                return 1 in squares
            else:
                squares.add(my_sum)

            m = my_sum


"""
Results:
Runtime: 36 ms, faster than 47.52% of Python3 online submissions for Happy Number.
Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Happy Number.
"""