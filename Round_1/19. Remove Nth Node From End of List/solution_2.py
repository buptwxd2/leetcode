# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head

        step = 0
        while fast and step < n:
            fast = fast.next
            step += 1

        if fast is None and step == n:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

"""
Results:
Runtime: 28 ms, faster than 89.44% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.7 MB, less than 87.48% of Python3 online submissions for Remove Nth Node From End of List.
"""