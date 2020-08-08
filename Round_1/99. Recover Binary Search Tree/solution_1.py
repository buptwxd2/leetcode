# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        pass

        results = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            results.append(root.val)
            inorder(root.right)

        inorder(root)

        mis_compare = []
        for i in range(len(results) - 1):
            if results[i] > results[i + 1]:
                mis_compare.append(i)

        if len(mis_compare) == 1:
            x, y = results[mis_compare[0]], results[mis_compare[0] + 1]
        else:
            x, y = results[mis_compare[0]], results[mis_compare[1] + 1]

        two_nodes = []

        def find_two_nodes(root, x, y):
            if not root:
                return

            if root.val == x or root.val == y:
                two_nodes.append(root)
            find_two_nodes(root.left, x, y)
            find_two_nodes(root.right, x, y)

        find_two_nodes(root, x, y)

        x_node, y_node = two_nodes
        tmp_node_val = x_node.val
        x_node.val = y_node.val
        y_node.val = tmp_node_val

        return

"""
Results:
Referred to https://leetcode-cn.com/problems/recover-binary-search-tree/solution/hui-fu-er-cha-sou-suo-shu-by-leetcode-solution/
Runtime: 76 ms, faster than 81.88% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.2 MB, less than 29.37% of Python3 online submissions for Recover Binary Search Tree.
"""