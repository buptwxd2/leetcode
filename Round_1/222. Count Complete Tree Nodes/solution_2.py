# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # BFS
        if not root:
            return 0

        queue = [root]
        num = 0
        break_in_advance = False

        while queue:
            nodes = len(queue)

            for _ in range(nodes):
                node = queue.pop(0)
                num += 1
                if node.left:
                    queue.append(node.left)
                else:
                    break_in_advance = True
                    break

                if node.right:
                    queue.append(node.right)
                else:
                    break_in_advance = True
                    break

            if break_in_advance:
                return num + len(queue)

        return num

"""
Results:
BFS way
Runtime: 112 ms, faster than 16.79% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.3 MB, less than 11.76% of Python3 online submissions for Count Complete Tree Nodes.
"""