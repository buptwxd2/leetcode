# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # bfs
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = []
        queue.append(root)
        depth = 0

        while queue:
            lvl_num = len(queue)

            depth += 1
            for _ in range(lvl_num):
                top = queue.pop(0)
                if not top.left and not top.right:
                    print(depth)
                    return depth

                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)


"""
Results:
BFS way
Runtime: 52 ms, faster than 45.29% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15 MB, less than 73.02% of Python3 online submissions for Minimum Depth of Binary Tree.
"""