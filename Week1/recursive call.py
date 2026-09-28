def fact(n):
    if n==0 or n==1:
        return 1
    return fact(n-1)*n

n=int(input("Enter the number of parcels:"))
result=fact(n)
print("The number of ways to arrange n different parcels are:",result)
