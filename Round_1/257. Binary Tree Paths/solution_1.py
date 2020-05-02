# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def return_list(root):
            if not root:
                return []

            if not root.left and not root.right:
                return [[root.val]]

            left_lists = return_list(root.left)
            right_lists = return_list(root.right)

            merged_list = left_lists + right_lists
            for sub_list in merged_list:
                sub_list.insert(0, root.val)

            return merged_list

        my_lists = return_list(root)
        x = []
        for sub_list in my_lists:
            y = "->".join([str(i) for i in sub_list])
            x.append(y)

        return x

"""
Results:
Runtime: 56 ms, faster than 5.51% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14.1 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
"""