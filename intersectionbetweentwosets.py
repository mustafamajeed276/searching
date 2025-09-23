A1 = [1, 2, 4, 7, 9, 10, 6]
A2 = [2, 3, 6, 8, 34, 10, 890]

m = len(A1)
n = len(A2)

i, j = 0, 0
while i < m and j < n:

    if A1[i] < A2[j]:
        i += 1
    elif A2[j] < A1[i]:
        j += 1
    else:
        print(A2[j], end=" ")
        j += 1
        i += 1        