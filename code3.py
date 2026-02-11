class Mentor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.first_name} Фамилия: {self.last_name}'


class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = {}

    def average_rating(self):
        """Средняя оценка за лекции по всем курсам"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f'Имя: {self.first_name} Фамилия: {self.last_name} Средняя оценка за лекции: {self.average_rating()}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() < other.average_rating()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() <= other.average_rating()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() == other.average_rating()
        return NotImplemented


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

    def average_grade(self):
        """Средняя оценка за домашние задания по всем курсам"""
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        return (f'Имя: {self.first_name} Фамилия: {self.last_name} '
                f'Средняя оценка за домашние задания: {self.average_grade()} '
                f'Курсы в процессе изучения: {courses_in_progress_str} '
                f'Завершенные курсы: {finished_courses_str}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented


# ---------- ПРОВЕРКА ----------
print('=== Проверка Reviewer ===')
reviewer = Reviewer('Пётр', 'Петров')
print(reviewer)
print()

print('=== Проверка Lecturer ===')
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Анна', 'Смирнова')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'Java']

# Оцениваем лекторов
student.rate_lecture(lecturer1, 'Python', 7)
student.rate_lecture(lecturer1, 'Python', 9)
student.rate_lecture(lecturer2, 'Python', 10)
student.rate_lecture(lecturer2, 'Java', 8)

print(lecturer1)
print(lecturer2)
print()

print('=== Сравнение лекторов ===')
print(f'lecturer1 > lecturer2: {lecturer1 > lecturer2}')
print(f'lecturer1 < lecturer2: {lecturer1 < lecturer2}')
print(f'lecturer1 == lecturer2: {lecturer1 == lecturer2}')
print()

print('=== Проверка Student ===')
# Добавляем оценки студенту (от рецензента)
reviewer.courses_attached += ['Python']
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 7)

student.finished_courses += ['Введение в программирование']
print(student)
print()

print('=== Сравнение студентов ===')
student2 = Student('Петров', 'Сергей', 'М')
student2.courses_in_progress += ['Python']
student2.grades['Python'] = [5, 6, 7]
student2.finished_courses += ['Git']

print(f'student1 > student2: {student > student2}')
print(f'student1 < student2: {student < student2}')
print(f'student1 == student2: {student == student2}')