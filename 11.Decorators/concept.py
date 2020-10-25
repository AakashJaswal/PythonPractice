# bellow fun() actually accept and return function
# the accepted function is being called in the function returned
# hence when you call x i.e., x() it execute wrapper()
def fun(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")

    return wrapper


def func2():
    print("called function 2")


x = fun(func2)
# print(x)   this print signature of wrapper functions <function fun.<locals>.Wrapper at 0x00EB7850>

# if you need result of the function call x
# x()
# Functions are first class object i.e., you can ref them call them pass them as arguments


# now i can write below line
# func2 = fun(func2)
# below call will now call out intended decorator function with itself as an arg.
# previously we were storing this in x and then calling x.
# func2()


# DECORATOR make this possible with an annotation

