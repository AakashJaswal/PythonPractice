import functools
def decorator_func(f):
    @functools.wraps(f)
    def inner_func(*args):
        print("Initial common task")
        return_value = f(*args)
        print(f"Called function {f.__name__} with argument {args} and got response {return_value}")
        print("Ended common task")
        return return_value

    return inner_func


@decorator_func
def func1(x, y):
    return x + y


sum = func1(2, 5)

print(sum)
