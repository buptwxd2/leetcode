class Solution:
    def calPoints(self, ops: List[str]) -> int:
        my_stack = []

        for op in ops:
            if op == 'C':
                my_stack.pop(-1)
            elif op == 'D':
                my_stack.append(my_stack[-1] * 2)
            elif op == '+':
                my_stack.append(my_stack[-1] + my_stack[-2])
            else:
                my_stack.append(int(op))

        return sum(my_stack)

"""
Results:
Runtime: 32 ms, faster than 95.90% of Python3 online submissions for Baseball Game.
Memory Usage: 14.2 MB, less than 10.00% of Python3 online submissions for Baseball Game.
"""