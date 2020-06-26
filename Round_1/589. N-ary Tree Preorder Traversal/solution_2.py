"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        my_stack = []
        seen = set()
        output = []

        # initialize
        my_stack.append(root)
        seen.add(root)

        while my_stack:
            curr_top_node = my_stack.pop(-1)
            output.append(curr_top_node.val)

            if curr_top_node.children:
                for child in curr_top_node.children[::-1]:
                    my_stack.append(child)

        return output

"""
Results:
DFS
Runtime: 48 ms, faster than 89.31% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 15.7 MB, less than 29.35% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""