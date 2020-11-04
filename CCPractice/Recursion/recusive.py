def rec(n):
    if n<1:
        return 1
    else:
        return n*rec(n-1)

num = int(input("Enter a number to find factorial for: "))

print(rec(num))