# Time Complexity: O(n log n)   Space Complexity: O(n)
def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merging(left, right)
def merging(A,B):
    merge=[0]*(len(A)+len(B))
    i=j=k=0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merge[k] = A[i]
            i=i+1
            k=k+1
        else:
            merge[k] = B[j]
            j=j+1
            k=k+1
    while i < len(A):
        merge[k] = A[i]
        i=i+1
        k=k+1
    while j < len(B):
        merge[k] = B[j]
        j=j+1
        k=k+1
    return merge
arr=[12,34,54,1,2,4,1,5]
print(divide(arr))


    