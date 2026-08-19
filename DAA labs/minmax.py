## Time Complexity: O(n)   Space Complexity: O(n)
def minmax(arr):
    if len(arr)==1:
        return(arr[0],arr[0])
    mid=len(arr)//2
    min1,max1=minmax(arr[:mid])
    min2,max2=minmax(arr[mid:])
    if(min1<min2):
        final_min= min1
    else:
        final_min= min2
    if(max1>max2):
        final_max= max1
    else:
        final_max= max2
        return final_min,final_max
    arr=[6,3,5,2,4,7,8]
    print(minmax(arr))
    
    
