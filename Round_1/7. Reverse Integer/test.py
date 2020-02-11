class Solution:
    def firstUniqChar(self, s: str) -> int:
        deduped_chars = set()
        unique_char_dict = {}

        for idx, char in s:
            if char in deduped_chars:
                unique_char_dict.pop(char, None)
            else:
                deduped_chars.add(char)
                unique_char_dict[char] = idx

        return min(unique_char_dict.vaules) if unique_char_dict else -1