# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        def bfs(root):
            if not root:
                return 0

            my_queue = []

            # initialize
            my_queue.append(root)
            my_nodes = [1]
            max_width = 0

            while my_queue:
                # Remove the leading None
                while my_queue and my_queue[0] is None:
                    my_queue.pop(0)
                    my_nodes.pop(0)

                # Remove the tailing None
                while my_queue and my_queue[-1] is None:
                    my_queue.pop(-1)
                    my_nodes.pop(-1)

                if my_nodes:
                    curr_width = my_nodes[-1] - my_nodes[0] + 1
                    if curr_width > max_width:
                        max_width = curr_width

                for _ in range(len(my_queue)):
                    curr_node = my_queue.pop(0)
                    node_num = my_nodes.pop(0)

                    if curr_node:
                        my_queue.append(curr_node.left)
                        my_nodes.append(2 * node_num)
                        my_queue.append(curr_node.right)
                        my_nodes.append(2 * node_num + 1)

            return max_width

        return bfs(root)

"""
Results:
level-order traversal
Runtime: 40 ms, faster than 72.12% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 14.4 MB, less than 39.75% of Python3 online submissions for Maximum Width of Binary Tree.
"""