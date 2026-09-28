def power(p, n):
    if n == 0:   # base case
        return 1 #joshikhaa laasya
    else:
        return p * power(p, n - 1)

p = int(input("Enter the value of the base: "))
n = int(input("Enter the number of years: "))
result = power(p, n)
print("The growth of an investment is:", result)
