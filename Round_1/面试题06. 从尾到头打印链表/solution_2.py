# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        sub_result = self.reversePrint(head.next)
        sub_result.append(head.val)

        return sub_result