class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Nếu min_stack chưa có gì, min chính là val.
        # Nếu đã có, min là số nhỏ hơn giữa val và min hiện tại ở đỉnh min_stack.
        current_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        # Xóa đồng thời cả 2 stack -> Luôn giữ đồng bộ 1:1
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]