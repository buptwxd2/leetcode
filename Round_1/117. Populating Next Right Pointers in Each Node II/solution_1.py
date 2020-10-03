"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        my_queue = []

        if not root: return

        # initialize
        my_queue.append(root)

        while my_queue:
            num = len(my_queue)

            first_node = my_queue.pop(0)
            if first_node.left:
                my_queue.append(first_node.left)
            if first_node.right:
                my_queue.append(first_node.right)

            prev_node = first_node

            for i in range(1, num):
                curr_node = my_queue.pop(0)
                prev_node.next = curr_node
                prev_node = curr_node

                if curr_node.left:
                    my_queue.append(curr_node.left)
                if curr_node.right:
                    my_queue.append(curr_node.right)

        return root

"""
Results
BFS(level order traversal)
Runtime: 36 ms, faster than 99.68% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
Memory Usage: 15.1 MB, less than 9.89% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
"""