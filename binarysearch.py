def binarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1


arr = [2, 10, 3, 4, 20, 11, 40, 50, 5, 12, 70]
x = 70

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is prsent at index {}".format(x, result))
else:
    print("Element is not present in array")    