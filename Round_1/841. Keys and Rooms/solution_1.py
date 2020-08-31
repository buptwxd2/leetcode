class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def bfs(start_node):
            visited = set()

            my_queue = [start_node]
            visited.add(start_node)

            results = []

            while my_queue:
                curr_top = my_queue.pop(0)
                results.append(curr_top)

                for neighbor in rooms[curr_top]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        my_queue.append(neighbor)

            return results

        results = bfs(0)

        return len(results) == len(rooms)

"""
Results:
BFS
Runtime: 68 ms, faster than 79.44% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.2 MB, less than 46.62% of Python3 online submissions for Keys and Rooms.
"""