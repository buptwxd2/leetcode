# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root:
            return []

        results = []

        my_queue = []
        visited = []

        my_queue.append(root)

        while my_queue:
            count = len(my_queue)  # node of this level

            level_sum = 0
            for i in range(count):
                curr_node = my_queue[i]
                level_sum += curr_node.val
                if curr_node.left and curr_node.left not in visited:
                    my_queue.append(curr_node.left)
                if curr_node.right and curr_node.right not in visited:
                    my_queue.append(curr_node.right)

                visited.append(curr_node)

            results.append(level_sum / count)

            # pop out this level of nodes
            for i in range(count):
                my_queue.pop(0)

        return results

"""
Results:
Runtime: 604 ms, faster than 5.67% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16 MB, less than 67.58% of Python3 online submissions for Average of Levels in Binary Tree.
"""