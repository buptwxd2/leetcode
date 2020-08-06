# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []

        def dfs(root, path):
            if not root.left and not root.right:
                tmp = 0
                for val in path:
                    tmp += val
                if tmp == sum:
                    results.append(path)

            if root.left:
                path_copy = path[:]
                path_copy.append(root.left.val)
                dfs(root.left, path_copy)

            if root.right:
                path_copy = path[:]
                path_copy.append(root.right.val)
                dfs(root.right, path_copy)

        if not root:
            return []

        dfs(root, [root.val])

        return results

"""
Results:
Using DFS way
Runtime: 72 ms, faster than 22.53% of Python3 online submissions for Path Sum II.
Memory Usage: 19.3 MB, less than 6.28% of Python3 online submissions for Path Sum II.
"""