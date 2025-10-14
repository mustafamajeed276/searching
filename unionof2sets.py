def unionOfArrays(A1, A2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if A1[i] < A2[j]:
            print(A1[i], end = " ")
            i += 1
        elif A2[j] < A1[i]:
            print(A2[j], end = " ")
            j += 1
        else:
            print(A2[j], end = " ")
            j += 1
            i += 1

    while i < m:
        print(A1[i], end = " ")
        i += 1

    while j < n:
        print(A2[j], end = " ")
        j += 1


A1 = [1, 3, 5, 7]
A2 = [2, 3, 4, 7]
m = len(A1)
n = len(A2)
unionOfArrays(A1, A2, m, n)                            