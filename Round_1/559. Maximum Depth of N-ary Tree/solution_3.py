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

        # dfs
        my_stack = []
        depth = 0
        max_depth = depth

        # initialize
        depth += 1
        my_stack.append([root, depth])
        depth += 1

        while my_stack:
            curr_node, curr_depth = my_stack.pop(-1)
            if curr_depth > max_depth:
                max_depth = curr_depth

            if curr_node.children:
                for child in curr_node.children:
                    my_stack.append([child, curr_depth + 1])

        return max_depth

"""
Results:
DFS way
Runtime: 44 ms, faster than 79.47% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 15.7 MB, less than 45.03% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""