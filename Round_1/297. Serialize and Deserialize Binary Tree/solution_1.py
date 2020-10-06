# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

            all_none = True
            for i in range(l):
                curr_node = my_queue.pop(0)
                if not curr_node:
                    output.append(None)
                    my_queue.append(None)
                    my_queue.append(None)
                else:
                    all_none = False
                    output.append(curr_node.val)
                    my_queue.append(curr_node.left)
                    my_queue.append(curr_node.right)

            if all_none:
                break

        # squeeze
        last_node = output[-1]
        while last_node is None:
            output.pop(-1)
            last_node = output[-1]

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

        nodes = [TreeNode(val) if val != 'null' else None for val in nodes]

        # insert a fake node for simplicy and consistency
        nodes.insert(0, None)

        for i in range(1, len(nodes)):
            if 2 * i < len(nodes) and nodes[i]:
                nodes[i].left = nodes[2 * i]
            if 2 * i + 1 < len(nodes) and nodes[i]:
                nodes[i].right = nodes[2 * i + 1]

        return nodes[1]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
Results:
最后一个case报： Time Limit Exceeded（感觉是浪费太多的空Node占用空间了，因为是按照满二叉树的形式去管理的），其他case都通过了
考虑更好的/更紧凑的管理方式
"""