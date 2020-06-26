"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        max_depth = 0

        def get_depth(root, depth):
            # recursive DFS
            nonlocal max_depth

            if not root:
                return

            if depth > max_depth:
                max_depth = depth

            if root.children:
                for child in root.children:
                    get_depth(child, depth + 1)

        get_depth(root, 1)

        return max_depth


"""
Results:
Recursive DFS
Runtime: 40 ms, faster than 92.72% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 15.7 MB, less than 41.38% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""