#  LEGB
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-it

def scope_test():
    def do_local():
        str = "create in local, wont show up in print"

    def do_non_local():
        nonlocal str
        str = "used non local, so will reflect in Enclosing Scope"

    def do_global():
        global str
        str = "will reflect in global, outside scope test def call"

    str = "created"
    do_local()
    print("After local assignment:", str)
    do_non_local()
    print("After nonlocal assignment:", str)
    do_global()
    print("After global assignment:", str)


scope_test()
print("outside scope test:", str)
