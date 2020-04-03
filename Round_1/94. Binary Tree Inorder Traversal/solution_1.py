# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        outputs = []

        outputs.extend(self.inorderTraversal(root.left))
        outputs.append(root.val)
        outputs.extend(self.inorderTraversal(root.right))

        return outputs

"""
Results：
Runtime: 28 ms, faster than 64.77% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
"""