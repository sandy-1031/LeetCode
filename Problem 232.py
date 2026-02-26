class MyQueue:

    def __init__(self):
        self.q = []        

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        ele = self.q.pop(0)
        return ele        

    def peek(self) -> int:
        return self.q[0]        

    def empty(self) -> bool:
        return len(self.q) == 0
        