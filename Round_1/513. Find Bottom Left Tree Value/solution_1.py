# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        my_queue = []
        seen = set()
        last_level_nodes = []

        # initialize
        my_queue.append(root)
        seen.add(root)

        while my_queue:
            last_level_nodes = my_queue.copy()
            curr_lvl_node_num = len(my_queue)

            for i in range(curr_lvl_node_num):
                node = my_queue[i]

                if node.left:
                    my_queue.append(node.left)
                if node.right:
                    my_queue.append(node.right)

            # remove current level
            for i in range(curr_lvl_node_num):
                my_queue.pop(0)

        return last_level_nodes[0].val

"""
Results:
利用BFS的思想
Runtime: 48 ms, faster than 48.08% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16 MB, less than 85.44% of Python3 online submissions for Find Bottom Left Tree Value.
"""