# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        return self.count_root_node(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    # count the path number equals with sum starting with the node: root
    def count_root_node(self, root, sum):
        if root is None:
            return 0

        # root.val is equal to the sum
        only_root = int(root.val == sum)

        # check the left sub-tree
        left_count = self.count_root_node(root.left, sum - root.val)

        # check the right sub-tree
        right_count = self.count_root_node(root.right, sum - root.val)

        return only_root + left_count + right_count

"""
Results:
Runtime: 1020 ms, faster than 10.63% of Python3 online submissions for Path Sum III.
Memory Usage: 14.8 MB, less than 56.49% of Python3 online submissions for Path Sum III
"""
