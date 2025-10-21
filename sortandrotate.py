#program to check if the arrayu is rotated and orted
arr = [3, 4, 5, 1, 2]
n = len(arr)
count = 0
#terating loop from 1 to lenght of array
for i in range(1, n):
    #comparing tems of array
    if(arr[i-1]>arr[i]):
        count += 1

# SPECAL CASE COMPARNG FRST ELEM,ENT  TO THE LAT ELEMENT
if(arr[n-1]>arr[0]):
    count += 1      

#drier code
print(count<=1)    