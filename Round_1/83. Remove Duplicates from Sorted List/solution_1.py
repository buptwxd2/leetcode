# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        slow = fast = head

        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val

            fast = fast.next

        slow.next = None

        return head

"""
Results:
Runtime: 44 ms, faster than 61.49% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.2 MB, less than 5.22% of Python3 online submissions for Remove Duplicates from Sorted List.
"""