class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        if not s:
            return s

        left = 0
        right = len(s) - 1

        my_list = list(s)

        while left < right:
            while left < right and my_list[left].lower() not in vowels:
                left += 1

            while left < right and my_list[right].lower() not in vowels:
                right -= 1

            # swap
            tmp = my_list[left]
            my_list[left] = my_list[right]
            my_list[right] = tmp
            left += 1
            right -= 1

        return "".join(my_list)

"""
Results:
Runtime: 56 ms, faster than 58.66% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14.7 MB, less than 6.67% of Python3 online submissions for Reverse Vowels of a String.
"""
