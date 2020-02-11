class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}

        for char in s:
            cnt = my_dict.setdefault(char, 0)
            cnt += 1
            my_dict[char] = cnt

        for idx, char in enumerate(s):
            if my_dict[char] == 1:
                return idx

        return -1