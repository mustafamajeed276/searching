A = [1, 2, 3, 78, 76, 45, 4, 9, 8, 0]

for i in range(1, len(A)):

    value = A[i]

    j = i - 1
    while j >=0 and value < A[j]:
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = value

print("Ascending Order")        
print(A)
reverseA = A[::-1]
print("Descending Order")
print(reverseA)