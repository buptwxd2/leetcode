# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def dfs(root, level, results=[]):
            if not root:
                return []

            # recursive dfs
            if len(results) < level + 1:
                results.insert(0, [])

            results[-(level + 1)].append(root.val)

            if root.left:
                dfs(root.left, level + 1, results)
            if root.right:
                dfs(root.right, level + 1, results)

        res = []
        dfs(root, 0, res)

        return res


"""
Results:
Recursive DFS way
Runtime: 40 ms, faster than 30.78% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.6 MB, less than 7.31% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""