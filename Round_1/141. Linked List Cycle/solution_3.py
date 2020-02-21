# using two pointers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast_p = slow_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next  # move 1 step
            fast_p = fast_p.next.next  # move 2 steps

            if slow_p == fast_p:
                return True

        return False
