# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # step 1, find the middle of the linked list
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # odd
        if fast:
            slow = slow.next  # ignore the middle node
        # else even, do nothing

        # step 3, reverse the half
        slow = self.reverseLinkedList(slow)
        # reset fast to head
        fast = head

        while slow:
            if fast.val != slow.val:
                return False
            else:
                fast = fast.next
                slow = slow.next

        return True

    def reverseLinkedList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next

            curr.next = prev
            prev = curr
            curr = next_node

        return prev
