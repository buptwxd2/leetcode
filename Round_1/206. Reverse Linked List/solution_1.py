# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head_copy = head

        if head is None or head.next is None:
            return head

        prev_node = head
        curr_node = head.next
        next_node = curr_node.next

        while next_node:
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next

        curr_node.next = prev_node

        head_copy.next = None

        return curr_node

s = Solution()

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)

node_1.next = node_2
node_2.next = node_3

node = s.reverseList(node_1)
while node:
    print(node.val)
    node = node.next

