def decoratorFunc(f):
    def innerFunc():
        print("Initial common task")
        f()
        print("Ended common task")

    return innerFunc


@decoratorFunc
def func1():
    print("Done the main task")


func1()

# Below
# @decoratorFunc
# def func1():
#     print("Done the main task")

# is equivalent to
# func1 = decoratorFunc(func1)
