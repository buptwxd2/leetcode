"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone_node = Node(node.val, [])
            visited[node] = clone_node

            clone_neighbors = []
            for neighbor in node.neighbors:
                clone_neighbor = dfs(neighbor)
                clone_neighbors.append(clone_neighbor)

            clone_node.neighbors = clone_neighbors

            return clone_node

        return dfs(node)

"""
Results:
DFS way
此题也可以用BFS来做，参考https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/
Runtime: 40 ms, faster than 72.43% of Python3 online submissions for Clone Graph.
Memory Usage: 14.2 MB, less than 19.22% of Python3 online submissions for Clone Graph.
"""