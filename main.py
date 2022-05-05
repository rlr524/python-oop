# Object-oriented Programming in Python

def hello():
    print("Hello, Madison")


print(type(hello))

# Simply by declaring my_name as a string, we are instantiating an object of the class str
# Because of that, we can call any method included in str on our object
my_name = "Madison"
print(my_name.upper())


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof")

    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 10)
d.bark()
print(d.add_one(5))
print(type(d))

d2 = Dog("Bill", 4)
print(f"Dog's name is {d.name}")
print(f"Dog two's name is {d2.name}")

print(f"Dog get name is {d.get_name()}")
print(f"Dog two get name is {d2.get_name()}")

print(f"{d.get_name()}'s age is {d.get_age()}")
print(f"{d2.get_name()}'s age is {d2.get_age()}")

d.set_age(11)
print(f"{d.get_name()}'s new age is {d.get_age()}")
