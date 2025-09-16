#program to reverse an array
A = [1, 2, 3, 4, 5, 6, 7]

# initialize start and end 
start = 0
end = len(A) - 1

# reverse a from start to end
while start < end:

    #swaapping the elements of an array to reverse the array
    #same array
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

# driver code
print("Revrersed Array")
print(A)