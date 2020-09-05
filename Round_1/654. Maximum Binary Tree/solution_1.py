# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        max_val = max(nums)
        max_idx = nums.index(max_val)

        left = nums[:max_idx]
        right = nums[max_idx + 1:]

        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root


"""
Results:
Runtime: 216 ms, faster than 82.94% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.2 MB, less than 39.92% of Python3 online submissions for Maximum Binary Tree.
"""