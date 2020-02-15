# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # Note, we don't have the head Node
        # Instead, we only have the node to be deleted

        node.val = node.next.val
        node.next = node.next.next

        return