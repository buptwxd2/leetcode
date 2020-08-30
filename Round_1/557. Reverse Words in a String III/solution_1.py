class Solution:
    def reverseWords(self, s: str) -> str:

        if not s:
            return s

        def reverse_one_word(s):
            if not s:
                return

            s = list(s)

            start = 0
            end = len(s) - 1

            while start < end:
                tmp = s[start]
                s[start] = s[end]
                s[end] = tmp

                start += 1
                end -= 1

            return ''.join(s)

        words = s.split(' ')
        reversed_words = [reverse_one_word(word) for word in words]

        return ' '.join(reversed_words)

"""
Results
Runtime: 72 ms, faster than 22.52% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.1 MB, less than 78.24% of Python3 online submissions for Reverse Words in a String III.
"""