# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        results = []

        my_queue = []
        # visited = []    # remove visited since it's not possible to duplicated with others in tree structure

        my_queue.append(root)

        while my_queue:
            count = len(my_queue)  # node of this level

            level_sum = 0
            for i in range(count):
                curr_node = my_queue[i]
                level_sum += curr_node.val
                if curr_node.left:
                    my_queue.append(curr_node.left)
                if curr_node.right:
                    my_queue.append(curr_node.right)

            results.append(level_sum / count)

            # pop out this level of nodes
            for i in range(count):
                my_queue.pop(0)

        return results

"""
Results:
Runtime: 48 ms, faster than 86.56% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 15.8 MB, less than 96.70% of Python3 online submissions for Average of Levels in Binary Tree.
"""