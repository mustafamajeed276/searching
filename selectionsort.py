A = [44, 25, 176, 176, 11]

for i in range(len(A)):

    min_id = i
    for j in range(i+1, len(A)):
        if A[min_id] > A[j]:
            min_id = j


    A[i], A[min_id] = A[min_id], A[i]


print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i], end=" ")