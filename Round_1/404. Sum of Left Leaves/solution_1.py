# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(root, left=False):
            if not root:
                return 0

            if not root.left and not root.right:
                if left:
                    return root.val
                else:
                    return 0

            return helper(root.left, True) + helper(root.right, False)

        return helper(root, False)

"""
Results:
Runtime: 32 ms, faster than 62.80% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.5 MB, less than 7.69% of Python3 online submissions for Sum of Left Leaves.
"""