def linearsearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = [1, 2, 3, 14, 5]
key = 14
result = linearsearch(arr, key)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)