# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 or l2

        node1 = l1
        node2 = l2

        if l1.val <= l2.val:
            head = l1
            node1 = node1.next
        else:
            head = l2
            node2 = node2.next

        curr_node = head
        while node1 and node2:
            if node1.val <= node2.val:
                curr_node.next = node1
                node1 = node1.next
            else:
                curr_node.next = node2
                node2 = node2.next

            curr_node = curr_node.next

        if node1:
            curr_node.next = node1
        if node2:
            curr_node.next = node2

        return head
