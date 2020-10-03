# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        my_stack = []

        results = []
        visited = set()

        # initialize
        my_stack.append(root)
        visited.add(root)

        while my_stack:
            curr_top = my_stack[-1]

            if not curr_top.left and not curr_top.right:
                my_stack.pop(-1)
                results.append(curr_top.val)
            else:
                left_done, right_done = False, False
                if curr_top.right and curr_top.right not in visited:
                    my_stack.append(curr_top.right)
                    visited.add(curr_top.right)
                else:
                    right_done = True

                if curr_top.left and curr_top.left not in visited:
                    my_stack.append(curr_top.left)
                    visited.add(curr_top.left)
                else:
                    left_done = True

                if left_done and right_done:
                    my_stack.pop(-1)
                    results.append(curr_top.val)

        return results

"""
Results
自研解法
Runtime: 32 ms, faster than 53.05% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 14.1 MB, less than 9.12% of Python3 online submissions for Binary Tree Postorder Traversal.
"""