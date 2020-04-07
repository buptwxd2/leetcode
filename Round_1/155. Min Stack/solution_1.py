class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Results:
Runtime: 812 ms, faster than 16.95% of Python3 online submissions for Min Stack.
Memory Usage: 17.6 MB, less than 5.36% of Python3 online submissions for Min Stack.
"""