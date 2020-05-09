class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []

        if len(A) == 1:
            return list(A[0])

        ref_dict = {}
        for char in A[0]:
            if char not in ref_dict:
                ref_dict[char] = A[0].count(char)

        keys_to_del = []

        for char in ref_dict:
            for other_str in A[1:]:
                if char not in other_str:
                    keys_to_del.append(char)
                    break
                else:
                    curr_cnt = other_str.count(char)
                    if curr_cnt < ref_dict[char]:
                        ref_dict[char] = curr_cnt

        # remove the keys
        for char in keys_to_del:
            ref_dict.pop(char)

        # convert to list
        results = []
        for char, cnt in ref_dict.items():
            for _ in range(cnt):
                results.append(char)

        return results

"""
Results:
Runtime: 36 ms, faster than 96.70% of Python3 online submissions for Find Common Characters.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Find Common Characters.
"""