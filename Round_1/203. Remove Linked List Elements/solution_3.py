# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        if not head.next:
            return head if head.val != val else None

        # more than one node
        if head.val == val:
            return self.removeElements(head.next)

        p = head
        while p.next:
            if p.next.val != val:
                p = p.next
            else:
                p.next = p.next.next

        return head

"""
Results:
Runtime: 68 ms, faster than 72.74% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 23 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
"""
