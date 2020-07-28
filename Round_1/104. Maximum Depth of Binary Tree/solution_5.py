# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # BFS

        if not root:
            return 0

        my_queue = [root]
        depth = 0

        while my_queue:

            node_num = len(my_queue)

            for _ in range(node_num):
                node = my_queue.pop(0)
                if node.left:
                    my_queue.append(node.left)
                if node.right:
                    my_queue.append(node.right)

            depth += 1

        return depth

"""
Results:
BFS way
Runtime: 48 ms, faster than 47.13% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.1 MB, less than 84.54% of Python3 online submissions for Maximum Depth of Binary Tree.
"""