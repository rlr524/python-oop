class Student:
    def __init__(self, name, age, grade_level, score):
        self.name = name
        self.age = age
        self.grade_level = grade_level
        self.score = score

    def get_score(self):
        return self.score

    def get_grade_level(self):
        return self.grade_level


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_score(self):
        value = 0
        for s in self.students:
            value += s.get_score()

        return value / len(self.students)


madison = Student("Madison", 18, "Freshman", 95)
olivia = Student("Olivia", 18, "Freshman", 88)
conan = Student("Conan", 19, "Sophomore", 75)

course = Course("Math", 2)
course.add_student(madison)
course.add_student(olivia)
# print(course.students[0].name)
for n in range(0, len(course.students)):
    print(f"{course.students[n].name}, {course.students[n].age}")

print(course.get_average_score())