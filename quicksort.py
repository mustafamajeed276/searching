# function to find the partition position

def partition(A, low, high):

    # choosing the rightmost element as pivot
    pivot = A[high]

    # pointer for the greater element
    i = low - 1

    # compare each element with the pivot
    for j in range(low, high):
        if A[j] <= pivot:
        #if element smaller than pivot is found
        #swap it with the greater element pointed by i
            i = i + 1

        # swapping element at i with element at j
            (A[i], A[j]) = (A[j], A[i])

    # swap the pivot element with the greater element specified by i
    (A[i + 1], A[high]) = (A[high], A[i + 1])

    #return the position from where partition is done
    return i + 1

# function to implement quick sort
def quicksSort(A,low,high):
    if low < high:
        # find pivot element such that
        # element smaller than the pivot are on the left
        # elements greater than the pivot are on the right
        pi = partition(A, low, high)

        # recursive call on the left of pivot
        quicksSort(A, low, pi - 1)

        # recursive call on the right of pivot
        quicksSort(A, pi + 1, high)

# driver code
A = [8, 17, 22, 12, 0, 9, 16]
print("Unsorted array: ")
print(A)

n = len(A)-1

quicksSort(A,0,n)

print("Sorted array: ")
print(A)