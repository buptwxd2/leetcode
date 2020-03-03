# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check_range(start, end):
            if start >= end:
                return start

            mid = (start + end) // 2
            if isBadVersion(mid):
                check_range(start, mid)
            else:
                check_range(mid + 1, end)

        return check_range(1, n)