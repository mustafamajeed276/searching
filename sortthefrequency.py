class Data:
    def __init__(self,value,index,count=0):
        self.value = value
        self.index = index
        self.count = count

def sortByFrequencyAndIndex(arr):
    if arr is None or len(arr) < 2:
        return

    hm={}
    
    
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)).count += 1

    values = [*hm.values()]    



    values.sort(key=lambda x: (-x.count, x.index))

    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1 


if __name__ == "__main__":

    arr = [3,3,3,3,3,3,1,1,1,1,5,5,5,87,87,87,87,2,2,2,98,98,98,0,0,0,0,1,1,1,4,4]
    print("Original Array:", arr)
    sortByFrequencyAndIndex(arr)            
print("Sorted Array:", arr)