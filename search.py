def search(arr, n, x):

    for i in range(0, n):
        if(arr[i] == x):
            return i


    return -1

arr = [2,3,4,10,40]
x = 310
n = len(arr)

result = search(arr, n, x)

if (result == -1):
    print("element is not present in array")
else: 
    print("element is present in array", result)    