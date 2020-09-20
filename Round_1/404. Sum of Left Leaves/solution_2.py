# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        results = []

        def dfs(root):
            if not root:
                return

            if is_leaf(root.left):
                results.append(root.left.val)

            dfs(root.left)

            dfs(root.right)

        def is_leaf(root):
            if not root:
                return False

            if not root.left and not root.right:
                return True

            return False

        dfs(root)

        return sum(results)

"""
Results
Runtime: 28 ms, faster than 91.31% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.5 MB, less than 30.36% of Python3 online submissions for Sum of Left Leaves.
"""