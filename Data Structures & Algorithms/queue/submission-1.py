class Deque:
    
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        if len(self.items) == 0:
            return True
        return False

    def append(self, value: int) -> None:
        self.items.append(value)

    def appendleft(self, value: int) -> None:
        newItems = [value]
        newItems.extend(self.items)
        self.items = newItems

    def pop(self) -> int:
        if not (self.isEmpty()):
            return self.items.pop(len(self.items) - 1)
        else:
            return -1

    def popleft(self) -> int:
        if not (self.isEmpty()):
            return self.items.pop(0)
        else:
            return -1
