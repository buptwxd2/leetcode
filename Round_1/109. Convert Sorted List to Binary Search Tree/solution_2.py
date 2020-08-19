# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        def get_mid(head):
            fast = slow = head
            prev = None

            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            prev.next = None

            return slow

        mid = get_mid(head)
        root_node = TreeNode(mid.val)
        root_node.left = self.sortedListToBST(head)
        root_node.right = self.sortedListToBST(mid.next)

        return root_node

"""
Results:
Runtime: 136 ms, faster than 68.87% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 17.3 MB, less than 94.96% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""