class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        tmp = float("infinity")
        for n in self.stack:
            tmp = min(tmp, n)
        return tmp
