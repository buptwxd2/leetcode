class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        results = []
        total_len = len(digits)

        def dfs(i, curr_result):
            if i == total_len:
                results.append("".join(curr_result))
                return

            for char in mapping[digits[i]]:
                curr_result.append(char)
                dfs(i + 1, curr_result)
                curr_result.pop(-1)

        if not digits:
            return []

        dfs(0, [])

        return results

"""
Results:
Back Tracking Algorithm(回溯算法)
Runtime: 32 ms, faster than 66.37% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.6 MB, less than 98.89% of Python3 online submissions for Letter Combinations of a Phone Number.
"""