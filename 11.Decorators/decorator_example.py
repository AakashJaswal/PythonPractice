def decorator_func(f):
    def inner_func():
        print("Initial common task")
        f()
        print("Ended common task")

    return inner_func


@decorator_func
def func1():
    print("Done the main task")


func1()

# Below
# @decorator_func
# def func1():
#     print("Done the main task")

# is equivalent to
# func1 = decorator_func(func1)
