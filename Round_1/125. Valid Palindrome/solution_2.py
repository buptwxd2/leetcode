# two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            else:
                if not s[left].isalnum():
                    left += 1

                if not s[right].isalnum():
                    right -= 1

        return True

"""
Results:
Runtime: 48 ms, faster than 61.57% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Valid Palindrome.
"""