A = [10, 3, 5, 8, 13, 15, 89, 897, 6, 7, 0]

for i in range(1, len(A)):

    value = A[i]

    j = i - 1
    while j >=0 and value < A[j]:
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = value

print("Sorted Array")        
for i in range(len(A)):
    print("%d" %A[i], end=" ")