## Time Complexity:bestcase O(n log n), Worst O(n**2)   Space Complexity:  O(log n), Worst O(n)
def partition(arr,start,end):
    pindex=start
    pivot=arr[end]
    for i in range (start,end):
        arr[i],arr[pindex]=arr[pindex],arr[i]
        pindex=pindex+1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex
def quicksort(arr,start,end):
    if (start<end):
        pi=partition(arr,start,end)
        quicksort=(arr,start,pi-1)
        quicksort=(arr,pi+1,end)
        return arr()
       

arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)