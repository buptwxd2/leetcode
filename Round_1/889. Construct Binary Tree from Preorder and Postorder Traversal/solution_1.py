# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        if not pre:
            return None

        root_val = pre[0]
        root = TreeNode(root_val)

        if len(pre) == 1:
            return TreeNode(root_val)

        left_root_val = pre[1]
        post_idx = post.index(left_root_val)

        left_len = post_idx + 1

        left_pre = pre[1:1 + left_len]
        right_pre = pre[1 + left_len:]

        left_post = post[:left_len]
        right_post = post[left_len:-1]

        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)

        return root

"""
Results
Runtime: 52 ms, faster than 81.41% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
Memory Usage: 14.2 MB, less than 5.19% of Python3 online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
"""