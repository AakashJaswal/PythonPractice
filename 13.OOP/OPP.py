class Animal:
    def __init__(self, color, age, type):
        self.color = color
        self.age = age
        self.type = type

    def speak(self):
        print(f"{self.type} go Mysterious Language")


class Dog(Animal):
    def __init__(self, color, age, type):
        Animal(color, age,type)
        self.type = type
    def speak(self):
        print(f"{self.type} go WOOF WOOF")

if __name__ == '__main__':
    noname = Animal("white", 2, "notsure")
    noname.speak()
    dog = Dog("Brown",3,"Dog")
    dog.speak()