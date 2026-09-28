def countdown(n):
    if n>=1:
        print(n)
        countdown(n-1)
    else:
        print("Launch!")

n=int(input("Enter the countdown Number:"))
countdown(n)
