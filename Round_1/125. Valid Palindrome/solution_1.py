class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_str = [c.lower() for c in s if c.isalnum()]

        total_len = len(valid_str)

        for i in range(total_len // 2):
            if valid_str[i] != valid_str[total_len - i - 1]:
                return False

        return True

# Results:
"""
Runtime: 48 ms, faster than 61.57% of Python3 online submissions for Valid Palindrome.
Memory Usage: 18.5 MB, less than 5.95% of Python3 online submissions for Valid Palindrome.
"""