# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        left_t = self.levelOrderBottom(root.left)
        right_t = self.levelOrderBottom(root.right)

        final = [[root.val]]
        import itertools
        for left, right in itertools.zip_longest(left_t[::-1], right_t[::-1], fillvalue=[]):
            item = left + right
            if item:
                final.insert(0, item)

        return final

