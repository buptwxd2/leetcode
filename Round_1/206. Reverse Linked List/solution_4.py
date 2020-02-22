# Actually same with solution_1, but it's more concise
# 实际上和solution_1很相似，只是更简洁

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            # save next node first
            next_node = curr.next
            # then change the direction/reverse
            curr.next = prev

            prev = curr
            curr = next_node

        return prev

