# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    results = []

    def postorderTraversal(self, root: TreeNode) -> List[int]:

        results = []

        def dfs(root):
            nonlocal results

            if not root:
                return []

            if root.left:
                results.extend(self.postorderTraversal(root.left))

            if root.right:
                results.extend(self.postorderTraversal(root.right))

            results.append(root.val)

            return results

        results = dfs(root)

        return results

"""
Results:
Runtime: 24 ms, faster than 92.70% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14.2 MB, less than 5.16% of Python3 online submissions for Binary Tree Postorder Traversal.
"""