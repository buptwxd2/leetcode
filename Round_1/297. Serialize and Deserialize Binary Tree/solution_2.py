# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'

        output = []
        my_queue = []

        # initialize
        my_queue.append(root)

        while my_queue:
            l = len(my_queue)

            for i in range(l):
                curr_node = my_queue.pop(0)
                if curr_node:
                    output.append(curr_node.val)
                    my_queue.append(curr_node.left)
                    my_queue.append(curr_node.right)
                else:
                    output.append('null')

        # squeeze
        while output[-1] == 'null':
            output.pop(-1)

        # to string
        output = ['null' if s is None else str(s) for s in output]

        return " ".join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == 'null':
            return None

        nodes = data.split()

        root = TreeNode(nodes[0])

        my_queue = [root]
        i = 1

        while my_queue and i < len(nodes):
            node = my_queue.pop(0)

            # left
            if nodes[i] != 'null':
                left = TreeNode(nodes[i])
                node.left = left
                my_queue.append(left)

            i += 1
            if i >= len(nodes):
                break

            # right
            if nodes[i] != 'null':
                right = TreeNode(nodes[i])
                node.right = right
                my_queue.append(right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
Results:
Runtime: 140 ms, faster than 51.61% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 18.4 MB, less than 73.71% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""