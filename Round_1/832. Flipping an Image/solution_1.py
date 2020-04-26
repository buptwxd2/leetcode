class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        tmp = []
        final = []

        for sub_list in A:
            tmp.append(reversed(sub_list))

        def invert(num):
            return 1 if num == 0 else 0

        for sub_list in tmp:
            sub_list = [invert(num) for num in sub_list]
            final.append(sub_list)

        return final



"""
Results:
Runtime: 84 ms, faster than 5.16% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.9 MB, less than 6.00% of Python3 online submissions for Flipping an Image.
"""