# There's no private variable but you can use _ prefix.
# __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam
# this is called name mangling (to avoid name clashes of names with names defined by subclasses)

# use @staticmethod for creating static method, can be called with class name can't use any class or object attr

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Dog(Animal):
    Dogs = []  # Used by all the instances i.e., Class variable

    def __init__(self, name, age, type):
        Animal.__init__(self, name, age)
        self.type = type
        self.Dogs.append(self)

    def speak(self):
        print(f"{self.name} go WOOF WOOF")

    @classmethod  # works like Java static i.e., access with class name and can only access class attribute
    def num_dogs(cls):
        return len(cls.Dogs)


if __name__ == '__main__':
    print(Dog.Dogs)
    print(Dog.num_dogs())
    no_name = Animal("white", 2)
    no_name.speak()
    dog = Dog("Brown", 3, "Labrador")
    dog2 = Dog("Jim", 3, "Canine")
    dog.speak()
    dog2.speak()
    print(Dog.Dogs)
    print(Dog.num_dogs())
