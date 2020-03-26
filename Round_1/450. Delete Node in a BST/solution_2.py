# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:   # both left and right exists
                # solution_2: 去到左子树中，找到值最大节点(一定没有右节点)，将root的右子树全部移到这个节点下的右子树
                largest = root.left
                while largest.right:
                    largest = largest.right

                largest.right = root.right

                return root.left

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

"""
Results:
Runtime: 76 ms, faster than 65.22% of Python3 online submissions for Delete Node in a BST.
Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Delete Node in a BST.
"""


