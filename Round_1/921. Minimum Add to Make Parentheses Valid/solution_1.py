class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0

        num = 0

        my_stack = []

        for char in S:
            if char == "(":
                my_stack.append(char)
            else:
                if not my_stack:
                    num += 1
                else:
                    my_stack.pop(-1)

        num += len(my_stack)

        return num


"""
Results:
Runtime: 32 ms, faster than 32.09% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
Memory Usage: 13.7 MB, less than 8.33% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
"""