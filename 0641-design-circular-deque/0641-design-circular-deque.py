class MyCircularDeque:

    def __init__(self, k: int):
        if k is not None:
            self.max_size = k
        else:
            self.max_size = 0
        self.deck = []

    def insertFront(self, value: int) -> bool:
        if len(self.deck)<self.max_size:
            temp = [value]
            temp.extend(self.deck)
            self.deck = temp
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deck)<self.max_size:
            self.deck.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deck:
            self.deck.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.deck:
            self.deck.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.deck==[]

    def isFull(self) -> bool:
        if len(self.deck):
            return len(self.deck)==self.max_size
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()