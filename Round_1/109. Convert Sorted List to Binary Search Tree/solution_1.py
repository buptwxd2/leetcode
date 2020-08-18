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

        def find_mid_node(head):
            if not head or not head.next:
                return head

            slow = head
            fast = head
            prev = head

            while fast.next and fast.next.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            return prev

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev_node = find_mid_node(head)
        # if not prev_node:
        #     return None
        mid_node = prev_node.next
        # if not mid_node:
        #     return None

        root_node = TreeNode(mid_node.val)

        r_head = mid_node.next
        prev_node.next = None

        l_root = self.sortedListToBST(head)
        r_root = self.sortedListToBST(r_head)

        root_node.left = l_root
        root_node.right = r_root

        return root_node

"""
Results:
Runtime: 164 ms, faster than 30.50% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 17.4 MB, less than 86.25% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""