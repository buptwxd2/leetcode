# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        results = []

        def pre_order(root):
            if not root:
                return

            pre_order(root.left)
            results.append(root.val)
            pre_order(root.right)

        pre_order(root)

        return results[k - 1]


"""
Results:

"""