class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def parse_str(S):
            my_stack = []

            for char in S:
                if char != "#":
                    my_stack.append(char)
                else:
                    if my_stack:
                        my_stack.pop(-1)

            return my_stack

        return parse_str(S) == parse_str(T)

"""
Results:
Runtime: 24 ms, faster than 90.10% of Python3 online submissions for Backspace String Compare.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
"""