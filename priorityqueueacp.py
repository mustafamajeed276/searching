import sys

class item:
    value = 0
    priority = 0

class GFG:

    pr = [None] * (100000)

    size = -1

    @staticmethod
    def enqueue(value, priority):
        GFG.size += 1
        GFG.pr[GFG.size] = item()
        GFG.pr[GFG.size].value = value
        GFG.pr[GFG.size].priority = priority

    @staticmethod
    def peek():
        highestPriority = -sys.maxsize
        ind = -1

        i = 0
        while i <= GFG.size:

            if highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value < GFG.pr[i].value:
                highestPriority = GFG.pr[i].priority
                ind = i
            elif highestPriority < GFG.pr[i].priority:
                highestPriority = GFG.pr[i].priority
                ind = i
            i+= 1

        return ind

    @staticmethod
    def dequeue():

        ind = GFG.peek()

        i = ind
        while i < GFG.size:
            GFG.pr[i] = GFG.pr[i + 1]
            i += 1

        GFG.size -= 1

    @staticmethod
    def main(args):

        GFG.enqueue(67, 2)
        GFG.enqueue(6, 7)
        GFG.enqueue(7, 77)
        GFG.enqueue(6767, 7676)

        ind = GFG.peek()
        print("Value with highest priority is " + str(GFG.pr[ind].value))

        GFG.dequeue()

        ind = GFG.peek()
        print("Value with highest priority is " + str(GFG.pr[ind].value))

        GFG.dequeue()

        ind = GFG.peek()
        print("Value with highest priority is " + str(GFG.pr[ind].value))

        GFG.dequeue()

        ind = GFG.peek()
        print("Value with highest priority is " + str(GFG.pr[ind].value))

if __name__ == "__main__":
    GFG.main(sys.argv)