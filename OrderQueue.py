from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__ (self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self,  i):
        while i // 2 > 0:
            if self.heapList[i].time < self.heapList[i//2].time:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) 
            if self.heapList[i].time > self.heapList[mc].time:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self, i):
        if i * 2 + 1> self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].time < self.heapList[i*2+1].time:
                return i * 2
            else:
                return 1 * 2 + 1
    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def processNextOrder(self):
        if self.currentSize == 0:
            raise QueueEmptyException
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval.getOrderDescription()


