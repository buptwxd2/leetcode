# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

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
Runtime: 208 ms, faster than 90.98% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 14.1 MB, less than 71.22% of Python3 online submissions for Maximum Binary Tree.
"""