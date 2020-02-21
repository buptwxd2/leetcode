# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        # find the tail node in the reversed sub linked list
        # see solution_3 for a more efficient way
        node = new_head
        while node.next:
            node = node.next

        node.next = head
        head.next = None

        return new_head
