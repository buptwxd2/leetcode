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
                    results.append(indexes)
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
                    indexes_cp = indexes[:]
                    indexes_cp.append(last_idx + i)
                    dfs(indexes_cp)
                else:
                    return

        dfs([])

        final_results = []
        for result in results:
            start = 0
            tmp_result = []
            for end in result:
                sub_s = s[start:end + 1]
                tmp_result.append(sub_s)
                start = end + 1

            tmp_result.append(s[start:])

            tmp_str = ".".join(tmp_result)
            final_results.append(tmp_str)

        return final_results

"""
Results:
Runtime: 44 ms, faster than 44.97% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 14 MB, less than 19.34% of Python3 online submissions for Restore IP Addresses.
"""