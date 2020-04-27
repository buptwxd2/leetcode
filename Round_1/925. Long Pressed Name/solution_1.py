class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 0 or len(typed) == 0:
            return name == typed

        if len(name) > len(typed):
            return False
        if len(name) == len(typed):
            return name == typed

        i = 0
        j = 0

        while i < len(name):
            # typed reaches the end while name does not yet -> return False
            if j >= len(typed):
                return False

            if name[i] != typed[j]:
                return False

            count_i = 1
            count_j = 1

            # count the number of this char: name[i]
            while i + 1 < len(name) and name[i + 1] == name[i]:
                count_i += 1
                i = i + 1

            # count the number of this char: typed[j]
            while j + 1 < len(typed) and typed[j + 1] == typed[j]:
                count_j += 1
                j = j + 1

            if count_i > count_j:
                return False

            i += 1
            j += 1

        # still other char in the ending of typed
        if j != len(typed):
            return False

        return True

"""
Results:
Runtime: 32 ms, faster than 52.07% of Python3 online submissions for Long Pressed Name.
Memory Usage: 13.7 MB, less than 14.29% of Python3 online submissions for Long Pressed Name.
"""