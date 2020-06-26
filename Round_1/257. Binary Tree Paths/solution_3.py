# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # recursive dfs
        if not root:
            return []

        results = []

        def dfs(node, sub_path):
            nonlocal results
            if not node.left and not node.right:
                results.append(sub_path)

            if node.left:
                dfs(node.left, sub_path + [node.left])
            if node.right:
                dfs(node.right, sub_path + [node.right])

        dfs(root, [root])

        outputs = []
        for result in results:
            my_str = "->".join(str(x.val) for x in result)
            outputs.append(my_str)

        return outputs


"""
Results:
Runtime: 36 ms, faster than 38.50% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.6 MB, less than 95.56% of Python3 online submissions for Binary Tree Paths.

"""