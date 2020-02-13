class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmn_prefix = ""
        if not strs:
            return cmn_prefix

        strs = sorted(strs)

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            if strs[0][i] == strs[-1][i]:
                cmn_prefix += strs[0][i]
            else:
                break

        return cmn_prefix

