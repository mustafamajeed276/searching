def sortArray(A):

    if len(A) <=1:
        return
    
    x = -1
    y = -1
    prev = A[0]

    for i in range(1, len(A)):

        if prev > A[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i

        prev = A[i]   


    swap(A, x, y)

def swap(a, i, j):

    temp = a[i]
    a[i] = a[j]
    a[j] = temp

if __name__ == "__main__":

    a = [1, 5, 3, 7]                     
    sortArray(a)
    print(a)