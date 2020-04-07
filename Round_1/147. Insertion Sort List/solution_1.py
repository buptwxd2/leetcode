# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        unsorted_node = head.next
        new_head = head
        new_head.next = None
        while unsorted_node:
            node_to_handle = unsorted_node.next
            new_head = self.sorted_list_insert(new_head, unsorted_node)
            unsorted_node = node_to_handle

        return new_head

    def sorted_list_insert(self, head, node_to_insert):
        p = head
        node_to_insert.next = None

        if p.val > node_to_insert.val:
            node_to_insert.next = p
            return node_to_insert

        while p.next:
            if p.next.val > node_to_insert.val:
                break
            else:
                p = p.next

        if p.next:
            node_to_insert.next = p.next
            p.next = node_to_insert
            return head
        else:
            p.next = node_to_insert
            return head

"""
Results:
Runtime: 3512 ms, faster than 5.02% of Python3 online submissions for Insertion Sort List.
Memory Usage: 15.7 MB, less than 25.00% of Python3 online submissions for Insertion Sort List.
"""