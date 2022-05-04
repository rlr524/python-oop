# Object-oriented Programming in Python

def hello():
    print("Hello, Madison")


print(type(hello))

# Simply by declaring my_name as a string, we are instantiating an object of the class str
# Because of that, we can call any method included in str on our object
my_name = "Madison"
print(my_name.upper())


class Dog:
    def bark(self):
        print("woof")


d = Dog()
d.bark()
print(type(d))
