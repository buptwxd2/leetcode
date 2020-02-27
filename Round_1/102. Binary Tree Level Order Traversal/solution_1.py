# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [[root.val]]

        if root.left and not root.right:
            left_t = self.levelOrder(root.left)
            left_t.insert(0, [root.val])
            return left_t

        if root.right and not root.left:
            right_t = self.levelOrder(root.right)
            right_t.insert(0, [root.val])
            return right_t

        left_t = self.levelOrder(root.left)
        right_t = self.levelOrder(root.right)

        if left_t and right_t:
            import itertools
            final = [[root.val]]
            for left, right in itertools.zip_longest(left_t, right_t, fillvalue=[]):
                item = left + right
                final.append(item)

            return final

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_1.left = node_2


s = Solution()
print(s.levelOrder(node_1))

"""
Results:
Runtime: 32 ms, faster than 73.68% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
"""

