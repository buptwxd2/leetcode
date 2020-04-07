# need to figure out the iterative solution

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

        my_queue = []
        outputs = []

        my_queue.extend([root.left, root, root.right])
        while my_queue:
            node = my_queue.pop(0)




"""
Results：

"""