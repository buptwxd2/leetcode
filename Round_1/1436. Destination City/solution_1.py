class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()
        srcs = set()

        for path in paths:
            src, dest = path

            cities.add(src)
            cities.add(dest)

            srcs.add(src)

        return (cities - srcs).pop()

"""
Results:
Runtime: 48 ms, faster than 96.61% of Python3 online submissions for Destination City.
Memory Usage: 14.1 MB, less than 5.07% of Python3 online submissions for Destination City.
"""