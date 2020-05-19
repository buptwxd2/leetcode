class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        choices = ['('] * n + [')'] * n
        results = []

        def back_tracking(curr_str, choices):
            if not choices:
                if is_valid(curr_str):
                    results.append(curr_str)

            for i, char in enumerate(choices):
                if i >= 1 and choices[i] == choices[i - 1]:
                    continue

                # make the choice
                new_str = curr_str + char
                new_choices = choices.copy()
                new_choices.remove(char)

                back_tracking(new_str, new_choices)

        def is_valid(s):
            pair = dict(zip('({[', ')}]'))

            stack = []

            for bracket in s:
                if bracket in pair.keys():
                    stack.append(bracket)
                else:
                    if not stack:
                        return False

                    top_item = stack.pop()
                    if pair[top_item] != bracket:
                        return False

            return not stack

        back_tracking('', choices)

        return results

"""
Results:
Runtime: 140 ms, faster than 5.20% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.
"""