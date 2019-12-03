#Recursion

def mySum(n):
    if n == 1:
        return 1
    else:
        return n * mySum(n-1)

print (mySum(5))