# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Note head points to the first node, there is no empty head node
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr_node = head
        prev_node = None

        while True:
            start_node, curr_node, actual_step = self.forwad_n_steps(curr_node, n)
            if actual_step < n:
                break
            else:
                prev_node = start_node

        if not prev_node:
            prev_head = head
            head = prev_head.next
            del prev_head

            return head

        # move prev_node forward actual_step steps
        _, node, _ = self.forwad_n_steps(prev_node, actual_step)
        node_to_remove = node.next
        node.next = node.next.next

        del node_to_remove

        return head

    def forwad_n_steps(self, node, n):
        start_node = node
        step = 0

        while node.next and step < n:
            node = node.next
            step += 1

        return start_node, node, step


head = ListNode(None)
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)


node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5

s = Solution()
head = node_1
head = s.removeNthFromEnd(head, 2)
while head:
    print (head.val)
    head = head.next
