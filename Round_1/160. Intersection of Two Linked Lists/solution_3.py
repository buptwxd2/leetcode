# use stack

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stack_a, stack_b = [], []

        p, q = headA, headB

        while p:
            stack_a.append(p)
            p = p.next

        while q:
            stack_b.append(q)
            q = q.next

        if not stack_a or not stack_b:
            return None

        node = None
        while stack_a and stack_b:
            p = stack_a.pop(-1)
            q = stack_b.pop(-1)

            if p == q:
                node = p
            else:
                break

        return node

""""
Results:
Runtime: 168 ms, faster than 56.14% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 28.1 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
"""