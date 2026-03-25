ar = [0 for _ in range(10)]
n = 10

front = -1
rear = -1

def enqueue(item):

    global n
    global rear
    global front
    if rear == n-1:
        print("Overflow", end = ' ')
        print("\n", end = '')
        return
    else:

        if front == -1 and rear == -1:
            front = 0
            rear = 0
        else:
            rear += 1

        ar[rear] = item
        print("element inserted")       

def dequeue():
    global n
    global rear
    global front

    if front == -1 or front > rear:
        print("Underflow", end = ' ')
        print("\n", end = '')
        return        
    else:
        item = ar[front]

        print("element deleted from queue is: ", end = ' ')
        print(item, end = ' ')
        print("\n", end = '')

        if rear == front:
            rear = -1
            front = -1
        else:
            front = front + 1

            front += 1

def display():
    global n
    global rear
    global front

    if front == -1:

        print("Queue is empty", end = ' ')
        print("\n", end = '')
        return
    else:
        print("Elemnts are : ", end = ' ')
        i = front
        while i <= rear:
            print(ar[i], end = ' ')
            print(" ", end = ' ')
            i += 1
        print("\n", end = '')

def fronte():
    global n
    global rear
    global gront

    if front == - 1:
        print("Queue is empty", end = ' ')
        print("\n", end = '')
        return
    else:

        print("front element is: ", end = ' ')
        print(ar[front], end = ' ')
        print("\n", end = '')


ch = None

print("1: Inserting element to queue(enqueue)", end = ' ')
print("\n", end = ' ')
print("2: Deleting element from queue(dequeue)", end = ' ')
print("\n", end = ' ')
print("3: Display front element of queue", end = ' ')
print("\n", end = ' ')
print("4: Display all the elements of queue", end = ' ')
print("\n", end = ' ')
print("5: Exit", end = ' ')
print("\n", end = ' ')
condition = True

while condition:

    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = int(input("Enter element to insert: "))
        enqueue(item)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        fronte()
    elif ch == 5:
        print("Exiting...", end = ' ')
        print("\n", end = ' ')
    else:
        print("Invalid choice", end = ' ')
        print("\n", end = ' ')
condition = ch!=5        