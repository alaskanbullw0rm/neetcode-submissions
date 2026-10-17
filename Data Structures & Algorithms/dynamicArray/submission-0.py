class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if (i < 0) or (i > self.capacity):
            return -1
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if (i > 0) or (i < self.capacity):
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        print("pushback")

    def popback(self) -> int:
        if (self.size > 0):   
            self.size -= 1
            pop = self.array[self.size]
            return pop
        else:
            return -1
 

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * self.capacity
        for i in range(self.size):
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        print(self.size)
        return self.size
    
    def getCapacity(self) -> int:
        print(self.capacity)
        return self.capacity
