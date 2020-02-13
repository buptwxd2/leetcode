class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        cmn_prefix = ''

        if not strs:
            return cmn_prefix

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            my_char = strs[0][i]

            if all(s[i] == my_char for s in strs):
                cmn_prefix += my_char
            else:
                return cmn_prefix

        return cmn_prefix

