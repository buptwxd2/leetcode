# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:   # both left and right exists
                # solution_1: 去到右子树中，找到值最小节点(一定没有左结点)，将root的左子树全部移到这个节点下的左子树
                smallest = root.right
                while smallest.left:
                    smallest = smallest.left

                smallest.left = root.left

                return root.right

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

"""
情况 1：当删除的节点没有左右子树，比如上图的 4、8、1
    这时直接删除即可，树依旧可以保持二叉搜索树的性质
情况 2：当删除的节点有左子树没有右子树，比如上图的 2
    这时我们只需要将整个左子树移到当前位置即可
    也就是将左子树的根节点放到删除节点的位置，其余不变
情况 3：当删除的节点没有左子树有右子树，比如上图的 6、7
    这时我们只需要将整个右子树移到当前位置即可
    也就是将右子树的根节点放到删除节点的位置，其余不变
情况 4：当删除的节点既有左子树又有右子树，比如上图的 5、3
    这时就有两种方法供选择：
        去到左子树中，找到值最大节点，将右子树全部移到这个节点下
        去到右子树中，找到值最小节点，将左子树全部移到这个节点下
"""


