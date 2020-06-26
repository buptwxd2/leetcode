# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def get_leaf_values(root, leaves=[]):
            if not root.left and not root.right:
                leaves.append(root.val)

            if root.left:
                get_leaf_values(root.left, leaves)

            if root.right:
                get_leaf_values(root.right, leaves)

        results_1, results_2 = [], []
        get_leaf_values(root1, results_1)
        get_leaf_values(root2, results_2)

        return results_1 == results_2

"""
Results:
Recursive DFS way
Runtime: 24 ms, faster than 97.87% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 13.8 MB, less than 74.31% of Python3 online submissions for Leaf-Similar Trees.
"""