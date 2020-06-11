# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        my_stack = []
        node = head

        while node:
            my_stack.append(node.val)
            node = node.next

        my_stack.reverse()

        return my_stack

