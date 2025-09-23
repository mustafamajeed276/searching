A = [9, 8, 3, 6, 7, 2, 5, 4, 1, 0, 10]

n = len(A)

interval = n // 2

while interval > 0:
    for i in range(interval, n):
        temp = A[i]
        j = i
        while j >= interval and A[j - interval] > temp:
            A[j] = A[j - interval]
            j -= interval

        A[j] = temp
    interval //= 2


print("Sorted array: ")
print(A)        