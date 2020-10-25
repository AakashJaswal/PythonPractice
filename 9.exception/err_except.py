# Raising exception
x = int(input('Enter a natural num: '))
if x < 0:
    raise Exception('Nope, I said NATURAL NUM')

# using assertion
assert (x >= 0), "X is not natural"
try:
    a = 5 / 0
except Exception as e:
    print(e)
else:
    # this is part of try catch, runs when there are no exception
    pass
finally:
    # use this for cleanup execute no matter what
    pass


# Create you own
class MyCustomException(Exception):
    pass


if True:
    raise MyCustomException('this is my custom exception')
