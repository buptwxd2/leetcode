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

        results = []
        results.append(root.val)
        for child in root.children:
            sub_result = self.preorder(child)
            results.extend(sub_result)

        return results

"""
Results:
recursive solution
Runtime: 64 ms, faster than 19.33% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 15.7 MB, less than 42.37% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""