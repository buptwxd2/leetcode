# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()

        p = head
        while p:
            if p in nodes:
                return p
            else:
                nodes.add(p)
                p = p.next

        return None

"""
Results:
Runtime: 52 ms, faster than 47.83% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
"""