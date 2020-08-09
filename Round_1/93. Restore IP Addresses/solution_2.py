class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []

        length = len(s)
        results = []

        def is_valid(s):
            if not s:
                return False

            if len(s) > 1 and s[0] == '0':
                return False

            num = int(s)

            if 0 <= num <= 255:
                return True

            return False

        def dfs(indexes):
            if len(indexes) == 3:
                remaining_s = s[indexes[-1] + 1:]
                if is_valid(remaining_s):
                    slice_objs = [slice(0, indexes[0]+1), slice(indexes[0]+1, indexes[1]+1), slice(indexes[1]+1, indexes[2]+1), slice(indexes[2]+1, length)]
                    sub_strs = [s[slice_obj] for slice_obj in slice_objs]
                    results.append(".".join(sub_strs))
                return

            if not indexes:
                for i in range(3):
                    sub_s = s[:i + 1]
                    if is_valid(sub_s):
                        indexes_cp = [i]
                        dfs(indexes_cp)
                    else:
                        return

                return

            last_idx = indexes[-1]

            for i in range(1, 1 + min(3, length - 1 - last_idx)):
                sub_s = s[last_idx + 1: last_idx + i + 1]
                if is_valid(sub_s):
                    indexes.append(last_idx + i)
                    dfs(indexes)
                    indexes.pop(-1)     # Key point: Need to undo -> This is the backtracking way
                else:
                    return

        dfs([])

        return results

"""
Results:
Runtime: 24 ms, faster than 99.11% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.8 MB, less than 60.69% of Python3 online submissions for Restore IP Addresses.
"""