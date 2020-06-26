# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # dfs + stack
        if not root:
            return []

        my_stack = []
        res = []

        # initialize
        my_stack.append([root, 0])

        while my_stack:
            node, level = my_stack.pop(-1)

            if len(res) < level + 1:
                res.insert(0, [])

            res[-(level + 1)].append(node.val)
            if node.right:
                my_stack.append([node.right, level + 1])
            if node.left:
                my_stack.append([node.left, level + 1])

        return res

"""
Results: 
DFS + stack
Runtime: 64 ms, faster than 6.69% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14 MB, less than 74.22% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""