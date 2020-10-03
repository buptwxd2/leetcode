# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def in_order(root):
            if not root:
                return []

            lefts = in_order(root.left)
            rights = in_order(root.right)

            return lefts + [root.val] + rights

        root1_in_order = in_order(root1)
        root2_in_order = in_order(root2)

        if not root1_in_order or not root2_in_order:
            return root1_in_order or root2_in_order

        p1, p2 = 0, 0

        results = []

        while p1 < len(root1_in_order) and p2 < len(root2_in_order):
            if root1_in_order[p1] <= root2_in_order[p2]:
                results.append(root1_in_order[p1])
                p1 += 1
            else:
                results.append(root2_in_order[p2])
                p2 += 1

        if p1 < len(root1_in_order):
            remaining = root1_in_order[p1:]
        else:
            remaining = root2_in_order[p2:]

        results += remaining

        return results

"""
Results:
Runtime: 520 ms, faster than 28.69% of Python3 online submissions for All Elements in Two Binary Search Trees.
Memory Usage: 22.7 MB, less than 5.00% of Python3 online submissions for All Elements in Two Binary Search Trees.
"""