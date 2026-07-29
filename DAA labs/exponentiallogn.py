#time complexity =o(log n).....space complexity=o(log n)... T(n)=2T(n/2)+O(1)

def power(x, n):
    if n == 0:
        return 1
    temp=power(x,n//2)
    if n % 2 == 0:
        return temp*temp
    else:
        return temp*temp*x
x,n=2,5
print(power(x,n))