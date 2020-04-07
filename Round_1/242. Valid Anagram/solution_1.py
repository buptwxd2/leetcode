class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_word_count = {}
        t_word_count = {}

        for char in s:
            num = s_word_count.setdefault(char, 0)
            num += 1
            s_word_count[char] = num

        for char in t:
            num = t_word_count.setdefault(char, 0)
            num += 1
            t_word_count[char] = num

        return s_word_count == t_word_count

s = Solution()
s.isAnagram("anagram", "nagaram")

"""
Results:
Runtime: 52 ms, faster than 37.48% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.2 MB, less than 9.38% of Python3 online submissions for Valid Anagram.
"""