# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = self.cal_len(head)
        if length == 0 or length == 1:
            return True

        curr_node = head
        steps = length - 1

        for _ in range(length // 2 ):
            compare_node = self.forward_steps(curr_node, steps)
            if curr_node.val != compare_node.val:
                return False
            else:
                curr_node = curr_node.next
                steps -= 2

        return True

    def cal_len(self, head):
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        return length

    def forward_steps(self, node, n):
        for _ in range(n):
            node = node.next

        return node

"""
Results: 	Time Limit Exceeded
逻辑应该还是没问题的，不过时间复杂度应该是O(n ** 2)，所以超时了
"""


s = Solution()

first_node_1 = ListNode(1)
first_node_2 = ListNode(2)
second_node_1 = ListNode(1)
second_node_2 = ListNode(2)

first_node_1.next = first_node_2
first_node_2.next = second_node_2
second_node_2.next = second_node_1


print(s.isPalindrome(first_node_1))