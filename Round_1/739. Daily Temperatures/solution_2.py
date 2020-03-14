class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        my_stack = []
        my_list = [0] * len(T)

        for idx, t in enumerate(T):
            while my_stack and my_stack[-1][1] < t:
                top_idx, top_t = my_stack.pop(-1)
                my_list[top_idx] = idx - top_idx

            my_stack.append((idx, t))

        return my_list

"""
Results:
Runtime: 484 ms, faster than 86.76% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.7 MB, less than 47.37% of Python3 online submissions for Daily Temperatures.
"""