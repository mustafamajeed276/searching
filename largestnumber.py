def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def largestNumber(nums):
    for i in range(len(nums)):
        tmp = 0
        for j in range(i):
            if not compare(nums[j], nums[tmp]):
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]        
    return str(int("".join(map(str, nums))))


arr = [8, 65, 90, 45, 82, 9]
print("Given array: ", arr)
print("Largest number is: ", largestNumber(arr))