# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a, len_b = 0, 0

        p = headA
        while p:
            len_a += 1
            p = p.next

        q = headB
        while q:
            len_b += 1
            q = q.next

        p, q = headA, headB
        if len_a > len_b:
            for _ in range(len_a - len_b):
                p = p.next
        else:
            for _ in range(len_b - len_a):
                q = q.next

        while p and q:
            if p == q:
                return p
            else:
                p = p.next
                q = q.next

        return None

"""
Results:
Runtime: 164 ms, faster than 73.54% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
"""
