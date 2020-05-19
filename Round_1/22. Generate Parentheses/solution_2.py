class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        choices = ['('] * n + [')'] * n
        results = []

        def back_tracking(curr_str, choices):
            if not choices:
                if is_valid(curr_str) and curr_str not in results:
                    results.append(curr_str)

            for char in choices:
                # if char in curr_str:
                #     continue

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
