class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        results = [0] * len(T)
        i = len(T) - 2
        for temperature in T[-2::-1]:
            j = i + 1
            while (T[j] <= temperature) and results[j] != 0:
                j += results[j]

            if T[j] > temperature:
                results[i] = j - i
            else:
                results[i] = 0

            i -= 1

        return results


"""
Results:
Runtime: 488 ms, faster than 81.91% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.6 MB, less than 73.68% of Python3 online submissions for Daily Temperatures.
"""