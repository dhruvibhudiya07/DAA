def merging(A,B):
    merge=[0]*(len(A)+len(B))
    i=j=k=0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merge[k] = A[i]
            i += 1
        else:
            merge[k] = B[j]
            j += 1
        k += 1
    while i < len(A):
        merge[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        merge[k] = B[j]
        j += 1
        k += 1
    return merge
A = [1,2,3,5,6,8,12,24,57,76]
B = [4,7,9,10,11,13,14,15,16,17]

print("The merging of 2 sorted arrays is:", merging(A, B))