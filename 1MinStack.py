class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val
        if len(self.min_stack) > 0:
            new_min = min(self.min_stack[-1], self.stack[-1])
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(7)
obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
