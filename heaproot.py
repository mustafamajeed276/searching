class MaxHeap:

    arr = []

    maxSize = 0

    heapSize = 0

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.heapSize = 0
        self.arr = [None] * maxSize

    def MaxHeapify(self, i):
        l = self.lChild(i)
        r = self.rChild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)

    def parent(self, i):
        return (i - 1) // 2

    def lChild(self, i):
        return 2 * i + 1

    def rChild(self, i):
        return 2 * i + 2

    def removeMax(self):
        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]

        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        self.MaxHeapify(0)

        return root

    def increaseKey(self, i, newVal):
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

    def getMax(self):
        return self.arr[0]

    def curSize(self):
        return self.heapSize

    def deleteKey(self, i):
        self.increaseKey(i, float("inf"))
        self.removeMax()

    def insertKey(self, x):
        if self.heapSize == self.maxSize:
            print("Overflow: Could not insertKey")
            return
        
        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)


if __name__ == "__main__":

    h = MaxHeap(10)

    k, i, n = 6, 0, 6
    print("Entered 6 keys: 67, 87, 92, 3, 57, 9, 56, 45, 1 \n")
    h.insertKey(67)
    h.insertKey(87)
    h.insertKey(92)
    h.insertKey(3)
    h.insertKey(57)
    h.insertKey(9)
    h.insertKey(56)
    h.insertKey(45)
    h.insertKey(1)

    print("The current heap size is: " + str(h.curSize()) + "\n")

    print("The maximum value is: " + str(h.getMax()) + "\n")

    h.deleteKey(5)

    print("After Deletion \n")
    print("The current heap size is: " + str(h.curSize()) + "\n")

    h.insertKey(15)
    h.insertKey(5)

    print("The current heap size is: " + str(h.curSize()) + "\n")
    print("The maximum value is: " + str(h.getMax()) + "\n")
    
    print(h.arr)