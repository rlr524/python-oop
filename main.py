# Object-oriented Programming in Python

def hello():
    print("Hello, Madison")


print(type(hello))

# Simply by declaring my_name as a string, we are instantiating an object of the class str
# Because of that, we can call any method included in str on our object
my_name = "Madison"
print(my_name.upper())


class Dog:

    def __init__(self, name):
        self.name = name
        print(name)

    def bark(self):
        print("woof")

    def add_one(self, x):
        return x + 1


d = Dog("Tim")
d.bark()
print(d.add_one(5))
print(type(d))

d2 = Dog("Bill")
