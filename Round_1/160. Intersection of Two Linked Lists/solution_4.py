# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB

        if not p or not q:
            return None

        while p != q:
            if not p:
                p = headB  # jump to head B
            else:
                p = p.next

            if not q:
                q = headA  # jump to head A
            else:
                q = q.next

        return p

"""
Results:
Runtime: 172 ms, faster than 37.22% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.2 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
"""