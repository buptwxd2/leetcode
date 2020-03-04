class Solution:
    def isValid(self, s: str) -> bool:
        pair = dict(zip('({[', ')}]'))

        stack = []

        for bracket in s:
            if bracket in pair.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False

                top_item = stack.pop()
                if pair[top_item] != bracket:
                    return False

        return not stack

"""
Results:
Runtime: 20 ms, faster than 97.74% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

基本思路：将open bracket(包括（，{，[)压栈，遇到ending bracket(包含），}，】)从stack pop，比较是否匹配
这好像是目前第一次遇到需要用到栈解决的题
"""