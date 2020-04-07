# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        # create a head node
        head_node = ListNode(0)
        head_node.next = head

        p = head_node
        while p.next:
            if p.next.val != val:
                p = p.next
            else:
                p.next = p.next.next

        return head_node.next

"""
Results:
Runtime: 68 ms, faster than 72.74% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 16.7 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
"""
