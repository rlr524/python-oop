class Person:
    # This is a class attribute; it's static, it's not defined with self
    # and can be called right on the class.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


tim = Person("Tim")
jill = Person("Jill")

# tim.number_of_people = 9
# print(jill.number_of_people)  # 0
# print(tim.number_of_people)  # 9
# print(Person.number_of_people)  # 0
print(Person.get_number_of_people())


class Math:
    # A static method has no connection to an object, it can be used without instantiating an object
    @staticmethod
    def add_five(n):
        return n + 5


print(Math.add_five(10))
