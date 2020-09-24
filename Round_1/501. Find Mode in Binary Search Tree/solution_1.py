# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return []

            nodes = [root.val]

            if root.left:
                nodes.extend(dfs(root.left))

            if root.right:
                nodes.extend(dfs(root.right))

            return nodes

        values = dfs(root)

        my_map = dict()

        for val in values:
            curr_cnt = my_map.setdefault(val, 0)
            curr_cnt += 1
            my_map[val] += 1

        if not my_map:
            return []

        max_frequency = max(my_map.values())

        modes = [val for val, cnt in my_map.items() if cnt == max_frequency]

        return modes

"""
Results:
Runtime: 44 ms, faster than 99.78% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 17.8 MB, less than 63.87% of Python3 online submissions for Find Mode in Binary Search Tree.
"""