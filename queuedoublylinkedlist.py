class GFG:

    class Node:
        data = 0
        perv = None
        next = None

        @staticmethod
        def getnode(data):
            newnode = GFG.Node()
            newnode.data = data
            newnode.perv = None
            newnode.next = None
            return newnode
        
    class Deque:
        front = None
        rear = None
        Size = 0

        def __init__(self):
            self.front = None
            self.rear = None
            self.Size = 0

        def isEmpty(self):
            return (self.front == None)

        def size(self):
            return self.Size

        def insertFront(self, data):
            newNode = GFG.Node.getnode(data)

            if (newNode == None):
                print("Overflow", end = "")
            else:

                if (self.front == None):
                    self.rear = newNode
                    self.front = newNode
                else:
                    newNode.next = self.front
                    self.front.perv = newNode
                    self.front = newNode

                self.Size += 1

        def insertRear(self, data):
            newNode = GFG.Node.getnode(data)

            if (newNode == None):
                print("Overflow", end = "")
            else:

                if (self.rear == None):
                    self.front = newNode
                    self.rear = newNode
                else:
                    newNode.perv = self.rear
                    self.rear.next = newNode
                    self.rear = newNode

                self.Size += 1

        def deleteFront(self):

            if (self.isEmpty()):
                print("Underflow", end = "")
            else:
                temp = self.front
                self.front = self.front.next

                if (self.front == None):
                    self.rear = None
                else:
                    self.front.perv = None

                self.Size -= 1

        def deleteRear(self):

            if (self.isEmpty()):
                print("Underflow", end = "")
            else:
                temp = self.rear
                self.rear = self.rear.perv

                if (self.rear == None):
                    self.front = None
                else:
                    self.rear.next = None

                self.Size -= 1\

        def getFront(self):

            if (self.isEmpty()):
                return -1
            return self.front.data
        
        def getRear(self):

            if (self.isEmpty()):
                return -1
            return self.rear.data
        
        def erase(self):