def rec(n):
    if n < 1:
        return 1
    else:
        return n * rec(n - 1)


def fib(counter, final, a=0, b=1):
    if counter >= final:
        print("")
        return 1
    else:
        print(a, end=" ")
        a, b, counter = b, a + b, counter + 1
        fib(counter, final, a, b)


def fib_hard_counter(final, a=0, b=1):
    if a >= final:
        print("")
        return 1
    else:
        print(a, end=" ")
        a, b = b, a + b
        fib_hard_counter(final, a, b)


num = int(input("Enter a number to find factorial for: "))
print(rec(num))

counter = int(input("Enter how many fibonacci no you need: "))
fib(0, counter)


hard_limit = int(input("Enter upto how many fibonacci no you need: "))
fib_hard_counter(hard_limit)