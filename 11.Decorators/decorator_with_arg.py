import functools
def my_decorator(repeate):
    def decorator_internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(repeate):
                resp = func(*args, **kwargs)
            return resp

        return wrapper

    return decorator_internal


@my_decorator(repeate=4)
def print_name(name):
    print(name)

print_name("Aakash")