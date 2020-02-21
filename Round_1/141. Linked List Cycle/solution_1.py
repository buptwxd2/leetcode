# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = []

        node = head
        while node:
            if node not in nodes:
                nodes.append(node)
                node = node.next
            else:
                return True

        return False

# speed is lower and space is O(n) since I created a list
# in solution_2, change list to set
