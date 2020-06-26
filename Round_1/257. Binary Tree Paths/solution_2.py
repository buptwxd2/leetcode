# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # dfs + stack

        if not root:
            return []

        my_stack = []
        results = []

        # initialize
        my_stack.append([root, [root]])

        while my_stack:
            node, sub_path = my_stack.pop(-1)
            if not node.left and not node.right:
                results.append(sub_path)

            if node.left:
                my_stack.append([node.left, sub_path + [node.left]])
            if node.right:
                my_stack.append([node.right, sub_path + [node.right]])

        outputs = []
        for result in results:
            my_str = "->".join(str(x.val) for x in result)
            outputs.append(my_str)

        return outputs
