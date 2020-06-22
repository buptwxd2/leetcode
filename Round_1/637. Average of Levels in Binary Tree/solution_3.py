# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use built-in Queue
from queue import Queue

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        results = []

        my_queue = Queue(maxsize=0)

        my_queue.put(root)

        while my_queue.qsize():
            count = my_queue.qsize()  # node of this level

            level_sum = 0
            for i in range(count):
                curr_node = my_queue.get()
                level_sum += curr_node.val
                if curr_node.left:
                    my_queue.put(curr_node.left)
                if curr_node.right:
                    my_queue.put(curr_node.right)

            results.append(level_sum / count)

        return results

"""
Results:
Runtime: 104 ms, faster than 5.67% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.1 MB, less than 50.48% of Python3 online submissions for Average of Levels in Binary Tree.
"""