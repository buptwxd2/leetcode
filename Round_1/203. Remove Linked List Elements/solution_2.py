# recursive way

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

        # more than one nodes
        if head.val != val:
            head.next = self.removeElements(head.next, val)
            return head
        else:
            return self.removeElements(head.next, val)

"""
Results:
Runtime: 144 ms, faster than 7.74% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 24.7 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
"""