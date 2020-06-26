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

        results = []

        for child in root.children:
            sub_result = self.postorder(child)
            results.extend(sub_result)
        results.append(root.val)

        return results

"""
Results:
recursive way
Runtime: 60 ms, faster than 24.83% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 15.8 MB, less than 11.82% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""