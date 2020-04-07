# use hash table
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        set_a = set()
        p = headA
        while p:
            set_a.add(p)
            p = p.next

        q = headB
        while q:
            if q in set_a:
                return q

            q = q.next

        return None

"""
Results:
Runtime: 164 ms, faster than 73.54% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.2 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.
"""