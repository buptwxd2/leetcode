class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        my_list = [[], [1], [1, 1]]
        for i in range(3, numRows + 1):
            sub_list = [1] * i
            for j in range(i):
                if j != 0 and j != i - 1:
                    sub_list[j] = my_list[i - 1][j - 1] + my_list[i - 1][j]

            my_list.append(sub_list)

        my_list.pop(0)
        return my_list

"""
Results:
Runtime: 28 ms, faster than 67.57% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
"""