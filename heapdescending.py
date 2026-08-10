import heapq

def sortarray(arr):
    minheap = []
    for num in arr:
        heapq.heappush(minheap, num)

    result = []
    while minheap:
        top = heapq.heappop(minheap)
        result.insert(0, top)
    return result

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 2]
    result = sortarray(arr)

    for num in result:
        print(num, end=' ')
    print()
