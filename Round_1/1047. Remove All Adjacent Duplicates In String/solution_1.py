class Solution:
    def removeDuplicates(self, S: str) -> str:

        my_stack = []

        for char in S:
            if not my_stack:
                my_stack.append(char)
            elif char == my_stack[-1]:
                my_stack.pop(-1)
            else:
                my_stack.append(char)

        return "".join(my_stack)


"""
Results:
Runtime: 72 ms, faster than 67.86% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
"""