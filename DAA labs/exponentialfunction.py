#time complexity =o(n).....space complexity=o(n)... T(n)=2T(n/2)+O(1)

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x,n//2)*power(x,n//2)
    else:
        return power(x,n//2)*power(x,n//2)*x
x,n=2,7
print(power(x,n))