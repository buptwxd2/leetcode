# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        # pre-order
        def pre_order(root):
            if not root:
                return []

            lefts = pre_order(root.left)
            rights = pre_order(root.right)

            return [root.val] + lefts + rights

        inorder = pre_order(root)

        return " ".join(str(val) for val in inorder)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = [int(x) for x in data.split()]

        def helper(vals):
            if not vals:
                return None

            root_val = vals[0]
            root = TreeNode(root_val)

            right_start_idx = 1
            while right_start_idx < len(vals) and vals[right_start_idx] < root_val:
                right_start_idx += 1

            left_vals = vals[1:right_start_idx]
            right_vals = vals[right_start_idx:]

            root.left = helper(left_vals)
            root.right = helper(right_vals)

            return root

        return helper(vals)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


"""
Results:
Runtime: 76 ms, faster than 81.66% of Python3 online submissions for Serialize and Deserialize BST.
Memory Usage: 18.2 MB, less than 42.90% of Python3 online submissions for Serialize and Deserialize BST.
"""