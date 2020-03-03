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

        for i in range(1, n + 1):
            if isBadVersion(i):
                return i

        return 0

"""
Naive Solution
Results:
Time Limit Exceeded
"""
