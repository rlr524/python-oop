class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")


class Fish (Pet):
    def eat(self):
        print("Eats some fish food")


class Cat (Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and I am {self.color}.")


class Dog (Pet):
    def speak(self):
        print("Bark")


class Goldfish (Fish):
    def eat(self):
        print("Eats some flakes")


p = Pet("Tim", 15)
p.show()
c = Cat("Bill", 10, "Brown")
c.show()
f = Goldfish("Bubbles", 1)
f.show()
f.eat()
