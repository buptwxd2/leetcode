class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def to_dict(tickets):
            mapping = {}

            for one_trip in tickets:
                start, end = one_trip
                mapping.setdefault(start, []).append(end)

            return mapping

        mapping = to_dict(tickets)

        total_len = len(tickets)

        def dfs(start, tmp_result):
            if start not in mapping or not mapping[start]:
                if len(tmp_result) == total_len + 1:
                    return tmp_result
                return

            # could not change to mapping[start].sort(), otherwise it would fail
            # because sorted would create a copy
            sorted_to_list = sorted(mapping[start])
            for next_stop in sorted_to_list:
                mapping[start].remove(next_stop)
                tmp_result.append(next_stop)
                worked = dfs(next_stop, tmp_result)
                if worked:
                    return worked
                tmp_result.pop(-1)
                mapping[start].append(next_stop)

        result = dfs('JFK', ['JFK'])

        return result

"""
Results:
Runtime: 88 ms, faster than 46.39% of Python3 online submissions for Reconstruct Itinerary.
Memory Usage: 14.3 MB, less than 33.07% of Python3 online submissions for Reconstruct Itinerary.
"""