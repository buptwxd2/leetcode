# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()

        node = head
        while node:
            if node not in nodes:
                nodes.add(node)
                node = node.next
            else:
                return True

        return False

# change to set, it's much faster
# but still space is still O(n) or even larger since i am using a hash table
