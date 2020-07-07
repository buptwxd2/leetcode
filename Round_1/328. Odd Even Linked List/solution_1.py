# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # counting from 1
        odd = head
        even_head = head.next
        even = even_head

        # this is the key point
        # 不能用 while odd and odd.next 来判断，否则下面会有条件错误
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head

"""
Runtime: 76 ms, faster than 15.15% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 15.8 MB, less than 35.15% of Python3 online submissions for Odd Even Linked List.
"""