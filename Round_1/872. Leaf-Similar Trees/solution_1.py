# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_values(root):
            if not root:
                return []

            # dfs way
            my_stack = []
            seen = set()
            leaves = []

            # initialize
            my_stack.append(root)

            while my_stack:
                node = my_stack.pop(-1)

                if node.left:
                    my_stack.append(node.left)
                if node.right:
                    my_stack.append(node.right)
                if not node.left and not node.right:
                    leaves.append(node.val)

            return leaves

        return get_leaf_values(root1) == get_leaf_values(root2)

"""
Results:
DFS way:
Runtime: 32 ms, faster than 68.26% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 13.9 MB, less than 27.16% of Python3 online submissions for Leaf-Similar Trees.
"""
