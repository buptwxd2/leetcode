# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)

        if length == 0:
            return None

        parent_idx = length // 2
        parent_node = TreeNode(nums[parent_idx])

        parent_node.left = self.sortedArrayToBST(nums[0:parent_idx])
        parent_node.right = self.sortedArrayToBST(nums[parent_idx + 1:])

        return parent_node


"""
Results:
Runtime: 68 ms, faster than 90.57% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""