# find if there is a pair in A[)..N-1] with given sum

# method

def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            #as equal i and j mean same elements
            if (i == j):
                continue

            # pair exists
            if (A[i] + A[j] == X):
                return [A[i], A[j]]
            
            # as the array is sorted
            if (A[i] + A[j] > X):
                break


    return 0

# array
arr = [2, 3, 5, 8, 9, 10, 11] 

# value to search
val = 17

print("pair with the sum equal to {} is - {}".format(val, isPairSum(arr, len(arr), val)))
