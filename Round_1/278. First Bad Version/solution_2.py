# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(n):
    if n <= 3:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check_range(start, end):
            if start == end:
                if isBadVersion(start):
                    return start
                else:
                    return -1

            mid = (start + end) // 2
            if isBadVersion(mid):
                return check_range(start, mid)
            else:
                return check_range(mid + 1, end)

        return check_range(1, n)

s = Solution()
print(s.firstBadVersion(5))

"""
Results:
Runtime: 24 ms, faster than 84.48% of Python3 online submissions for First Bad Version.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Bad Version.
"""