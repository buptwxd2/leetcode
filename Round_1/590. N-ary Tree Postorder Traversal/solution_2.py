"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
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
                for child in curr_top_node.children:
                    my_stack.append(child)

        return output[::-1]

"""
Results:
DFS
Runtime: 52 ms, faster than 69.48% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 15.7 MB, less than 32.41% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""