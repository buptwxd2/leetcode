# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        def bfs(root):
            queue = []
            reverse = False

            results = []

            queue.append(root)

            while queue:
                level_num = len(queue)

                tmp_list = []
                for _ in range(level_num):
                    curr_node = queue.pop(0)
                    tmp_list.append(curr_node.val)

                    if curr_node.left:
                        queue.append(curr_node.left)

                    if curr_node.right:
                        queue.append(curr_node.right)

                if reverse:
                    tmp_list.reverse()

                reverse = not reverse

                results.append(tmp_list)

            return results

        if not root:
            return []

        results = bfs(root)

        return results

"""
Results:
BFS
Runtime: 48 ms, faster than 29.71% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.1 MB, less than 27.60% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""