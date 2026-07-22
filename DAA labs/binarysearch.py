def binarysearch(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binarysearch(arr, mid + 1, high, key)
    else:
        return binarysearch(arr, low, mid - 1, key)
arr = [2, 3, 4, 5, 6, 7, 8, 9]   # Sorted array
key = 7
result = binarysearch(arr, 0, len(arr) - 1, key)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)