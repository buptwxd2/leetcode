class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def parse_complex(c):
            real, imaginary = c.split('+')
            real = int(real)
            imaginary = int(imaginary[:-1])

            return real, imaginary

        a_r, a_i = parse_complex(a)
        b_r, b_i = parse_complex(b)

        return str(a_r * b_r - a_i * b_i) + "+" + str(a_r * b_i + b_r * a_i) + 'i'


"""
Results:
Runtime: 28 ms, faster than 72.31% of Python3 online submissions for Complex Number Multiplication.
Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Complex Number Multiplication.
"""