"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        my_queue = []
        seen = set()
        outputs = []

        # initialize
        my_queue.append(root)
        seen.add(root)

        while my_queue:
            level_output = [node.val for node in my_queue]
            outputs.append(level_output)

            for _ in range(len(level_output)):
                node = my_queue.pop(0)
                if node.children:
                    for child in node.children:
                        my_queue.append(child)

        return outputs

"""
Results:
BFS
Runtime: 56 ms, faster than 53.35% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 15.6 MB, less than 72.91% of Python3 online submissions for N-ary Tree Level Order Traversal.
"""