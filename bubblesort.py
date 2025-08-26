# program to bubble sort

def BubbleSort(arr):
    n = len(arr)

    #transverse through the array
    for i in range(n):

        #last i elements are alrready in place
        for j in range(0, n-i-1):

            #transverse through the array from 0 to n-i-1
            #Swap if the element found is greater
            #than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


#driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

BubbleSort(arr)

print("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")