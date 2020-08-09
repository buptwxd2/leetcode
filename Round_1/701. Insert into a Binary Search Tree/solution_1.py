# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)

        if not root:
            return node

        curr_root = root

        while curr_root:

            if val > curr_root.val:
                if not curr_root.right:
                    curr_root.right = node
                    return root
                else:
                    curr_root = curr_root.right

            else:
                if not curr_root.left:
                    curr_root.left = node
                    return root
                else:
                    curr_root = curr_root.left

"""
Results:
Runtime: 140 ms, faster than 90.06% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 15.9 MB, less than 63.78% of Python3 online submissions for Insert into a Binary Search Tree.
"""