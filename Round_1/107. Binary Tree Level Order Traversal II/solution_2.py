# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # bfs + queue
        if not root:
            return []

        my_queue = []
        res = []

        # initialize
        my_queue.append(root)

        while my_queue:
            nodes = len(my_queue)  # this level of nodes
            tmp_res = []

            for _ in range(nodes):
                node = my_queue.pop(0)
                tmp_res.append(node.val)

                if node.left:
                    my_queue.append(node.left)
                if node.right:
                    my_queue.append(node.right)

            res.insert(0, tmp_res)

        return res

"""
Results:
BFS + queue way
Runtime: 36 ms, faster than 59.13% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14 MB, less than 84.72% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""