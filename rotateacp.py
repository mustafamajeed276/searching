
#Prgram to rotate a array

#nput array lenght and 'n'
def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

# rorare array to the left by one place
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp

def printArray(a, a_size):
    for i in range(a_size):
        print("% d" % a[i], end=" ")       
    print('\n')      

a = [9,10,1,2,3,4,5,6,7,8]
printArray(a, len(a))    
rotations(a, 2, len(a))
printArray(a, len(a))