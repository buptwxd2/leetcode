class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        valid_left = '('
        num = 0

        my_stack = []

        for char in S:
            if char == '(':
                num += 1

                if num == 1:
                    continue
                else:
                    my_stack.append(char)

            else:
                if num != 1:
                    my_stack.append(char)

                num -= 1

        return "".join(my_stack)

"""
Results:
Runtime: 28 ms, faster than 97.70% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
"""