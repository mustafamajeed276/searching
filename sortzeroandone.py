def sortZeroOne(A, n):

    count = 0
    for i in range(0, n):
        if(A[i] == 0):
            count = count + 1

    for i in range(0, count):
        A[i] = 0        

    for i in range(count, n):
        A[i] = 1


A = [0,1,0,0,1,0,1,0,1,1] 
n = len(A)


sortZeroOne(A, n)
print("Sorted Array is ", end = "")
for i in range(0, n):
    print(A[i], end = " ")