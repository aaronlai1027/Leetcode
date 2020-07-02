class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
            return self.min
        elif x <= self.min[-1]:
            self.min.append(x)  
        else:
            pass

    def pop(self) -> None:
        tmp_pop = self.stack.pop()
        if tmp_pop == self.min[len(self.min)-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
