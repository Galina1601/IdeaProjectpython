class Human:
    def _init_(self, name, age):
        self.name = name
        self.age = age



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Student: {self.name} {self.surname}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"{self.name} {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Проверка
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer,Mentor)) # True
print(lecturer.courses_attached)#[]
print(reviewer.courses_attached)#[]


