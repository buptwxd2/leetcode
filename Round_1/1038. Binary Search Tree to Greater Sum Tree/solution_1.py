# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        results = []

        def in_order(root):
            if not root:
                return []

            left_results = in_order(root.left)
            right_results = in_order(root.right)

            return left_results + [root.val] + right_results

        results = in_order(root)

        # pre_order
        def dfs(root):
            if not root:
                return

            root_idx = results.index(root.val)
            root.val = root.val + sum(results[root_idx + 1:])

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return root

"""
Results:
Runtime: 32 ms, faster than 62.42% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.1 MB, less than 5.49% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
"""