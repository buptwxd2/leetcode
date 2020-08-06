# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0

        def dfs(root, path):
            nonlocal result

            if not root.left and not root.right:
                path.append(root.val)

                path_num = int(''.join([str(x) for x in path]))

                result += path_num

                return

            if root.left:
                path_copy = path[:]
                path_copy.append(root.val)
                dfs(root.left, path_copy)

            if root.right:
                path_copy = path[:]
                path_copy.append(root.val)
                dfs(root.right, path_copy)

        if not root:
            return 0

        dfs(root, [])

        return result

"""
Results:
Runtime: 36 ms, faster than 52.76% of Python3 online submissions for Sum Root to Leaf Numbers.
Memory Usage: 13.7 MB, less than 96.75% of Python3 online submissions for Sum Root to Leaf Numbers.
"""