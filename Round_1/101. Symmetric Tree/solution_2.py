"""
TODO: iterative way, i guess to the help of queue

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.left_is_equal_to_right(root.left, root.right)

    def left_is_equal_to_right(self, left, right):
        queue1 = [left]
        queue2 = [right]

        while queue1 and queue2:
            left_node = queue1.pop(0)
            right_node = queue2.pop(0)

            # either node is None
            if left_node is None or right_node is None:
                if left_node == right_node:     # both nodes are None
                    continue
                else:
                    return False

            # neither node is None
            if left_node.val != right_node.val:
                return False
            else:
                queue1.extend([left_node.left, left_node.right])
                queue2.extend([right_node.right, right_node.left])

        return queue1 == queue2


node_9 = TreeNode(9)
left_42 = TreeNode(-42)
right_42 = TreeNode(-42)
left_76 = TreeNode(76)
right_76 = TreeNode(76)
left_13 = TreeNode(13)
right_13 = TreeNode(13)

node_9.left = left_42
node_9.right = right_42

left_42.right = left_76
right_42.left = right_76

left_76.right = left_13
left_76.right = right_13

s = Solution()
s.isSymmetric(node_9)

"""
Results:
Runtime: 20 ms, faster than 99.74% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
"""
