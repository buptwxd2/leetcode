"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        if not root.children:
            return 1
        else:
            return max(self.maxDepth(child) for child in root.children) + 1

"""
Results:
Runtime: 36 ms, faster than 97.67% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""