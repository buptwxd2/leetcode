class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        global_longest = 1

        current_longest_map = {}
        for i in range(len(s)):
            if s[i] in current_longest_map:
                current_longest_map = self.get_new_longest_map(current_longest_map, s[i])

            current_longest_map[s[i]] = i
            if len(current_longest_map) > global_longest:
                global_longest = len(current_longest_map)

        return global_longest

    def get_new_longest_map(self, longest_map, char):
        char_idx = longest_map[char]

        return dict([char, idx] for char, idx in longest_map.items() if idx > char_idx)

"""
Results:
Runtime: 560 ms, faster than 13.55% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.8 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""