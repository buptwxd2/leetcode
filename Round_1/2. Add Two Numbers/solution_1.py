# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        # calculate the head
        head_val = (l1.val + l2.val) % 10
        head = ListNode(head_val)
        curr_node = head
        carry_bit = (l1.val + l2.val) // 10

        p1 = l1.next
        p2 = l2.next

        while p1 and p2:
            curr_sum = p1.val + p2.val + carry_bit
            carry_bit = curr_sum // 10
            sum_node = ListNode(curr_sum % 10)
            curr_node.next = sum_node
            curr_node = sum_node

            p1 = p1.next
            p2 = p2.next

        if p1:
            while p1:
                curr_sum = p1.val + carry_bit
                carry_bit = curr_sum // 10
                sum_node = ListNode(curr_sum % 10)
                curr_node.next = sum_node
                curr_node = sum_node

                p1 = p1.next

        if p2:
            while p2:
                curr_sum = p2.val + carry_bit
                carry_bit = curr_sum // 10
                sum_node = ListNode(curr_sum % 10)
                curr_node.next = sum_node
                curr_node = sum_node

                p2 = p2.next

        if carry_bit != 0:
            end_node = ListNode(carry_bit)
            curr_node.next = end_node

        return head

