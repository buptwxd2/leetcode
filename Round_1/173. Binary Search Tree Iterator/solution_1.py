# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def in_order(root):
            if not root:
                return []

            lefts = in_order(root.left)
            rights = in_order(root.right)

            return lefts + [root.val] + rights

        inorder = in_order(root)

        self.inorder = inorder
        self.next_idx = 0
        self.length = len(inorder)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.inorder[self.next_idx]
        self.next_idx += 1

        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.next_idx < self.length

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


"""
Results
BST -> sorted array/list
Runtime: 84 ms, faster than 47.84% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.5 MB, less than 70.30% of Python3 online submissions for Binary Search Tree Iterator.
"""