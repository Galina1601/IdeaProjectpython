class Mentor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:
    def __init__(self, last_name, first_name, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in self.courses_in_progress and course in lecturer.courses_attached:
                if 1 <= grade <= 10:
                    if course not in lecturer.grades:
                        lecturer.grades[course] = []
                    lecturer.grades[course].append(grade)
                    return None
                else:
                    return 'Ошибка: оценка должна быть от 1 до 10'
            else:
                return 'Ошибка: курс не найден у студента или лектора'
        else:
            return 'Ошибка: оценивать можно только лектора'


# ---------- ПРОВЕРКА ----------
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))   # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))    # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6)) # Ошибка
print(lecturer.grades)  # {'Python': [7]}






