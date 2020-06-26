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

        # bfs
        my_queue = []
        depth = 0

        # initialize
        my_queue.append(root)
        while my_queue:
            depth += 1
            node_num = len(my_queue)

            for _ in range(node_num):
                node = my_queue.pop(0)
                if node.children:
                    for node in node.children:
                        my_queue.append(node)

        return depth

"""
Results:
BFS way:
Runtime: 64 ms, faster than 13.51% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 15.7 MB, less than 48.48% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""