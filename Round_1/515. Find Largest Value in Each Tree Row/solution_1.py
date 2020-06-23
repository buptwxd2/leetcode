# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        my_queue = deque()
        visited = []
        results = []

        # initilize
        my_queue.append(root)

        while my_queue:
            count = len(my_queue)  # count of this level

            level_max = my_queue[0].val

            for i in range(count):
                curr_node = my_queue.popleft()
                if curr_node.val > level_max:
                    level_max = curr_node.val

                if curr_node.left:
                    my_queue.append(curr_node.left)
                if curr_node.right:
                    my_queue.append(curr_node.right)

            results.append(level_max)

        return results


"""
Results:
Runtime: 40 ms, faster than 96.24% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.1 MB, less than 40.98% of Python3 online submissions for Find Largest Value in Each Tree Row.
"""