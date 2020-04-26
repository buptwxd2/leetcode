# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []

        for list_node in lists:
            while list_node:
                heapq.heappush(min_heap, list_node.val)
                list_node = list_node.next

        head_node = ListNode(0)
        curr_node = head_node

        while min_heap:
            min_val = heapq.heappop(min_heap)
            min_node = ListNode(min_val)
            curr_node.next = min_node
            curr_node = curr_node.next

        return head_node.next

"""
Results:
Runtime: 140 ms, faster than 35.37% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.9 MB, less than 10.60% of Python3 online submissions for Merge k Sorted Lists.
"""