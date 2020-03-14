class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_stack = []
        my_dict = {}

        for num in nums2:
            while my_stack and my_stack[-1] < num:
                top_num = my_stack.pop(-1)
                my_dict[top_num] = num

            my_stack.append(num)

        for num in my_stack:
            my_dict[num] = -1

        my_list = [my_dict[num] for num in nums1]

        return my_list

"""
Results:
Runtime: 48 ms, faster than 65.35% of Python3 online submissions for Next Greater Element I.
Memory Usage: 13.2 MB, less than 77.78% of Python3 online submissions for Next Greater Element I.
"""