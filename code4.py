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
            return None
        return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.first_name} Фамилия: {self.last_name}'


class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = {}

    def average_rating(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return (f'Имя: {self.first_name} Фамилия: {self.last_name} '
                f'Средняя оценка за лекции: {self.average_rating()}')

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
                return 'Ошибка: оценка должна быть от 1 до 10'
            return 'Ошибка: курс не найден у студента или лектора'
        return 'Ошибка: оценивать можно только лектора'

    def average_grade(self):
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


# ---------- ФУНКЦИИ ДЛЯ ЗАДАНИЯ 4 ----------

def average_grade_for_course_students(students_list, course_name):
    """
    Подсчитывает среднюю оценку за ДЗ для всех студентов по конкретному курсу
    """
    total_grades = []
    for student in students_list:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    if not total_grades:
        return 0.0
    return round(sum(total_grades) / len(total_grades), 1)


def average_grade_for_course_lecturers(lecturers_list, course_name):
    """
    Подсчитывает среднюю оценку за лекции для всех лекторов по конкретному курсу
    """
    total_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    if not total_grades:
        return 0.0
    return round(sum(total_grades) / len(total_grades), 1)


# ---------- ПОЛЕВЫЕ ИСПЫТАНИЯ ----------

def main():
    print('=== ЗАДАНИЕ 4: ПОЛЕВЫЕ ИСПЫТАНИЯ ===\n')

    # 1. Создаём по 2 экземпляра каждого класса
    print('--- Создаём экземпляры ---')

    # Студенты
    student1 = Student('Иванов', 'Иван', 'М')
    student2 = Student('Петрова', 'Анна', 'Ж')
    student1.courses_in_progress += ['Python', 'Git']
    student2.courses_in_progress += ['Python', 'Java']
    student1.finished_courses += ['Введение в программирование']
    student2.finished_courses += ['Основы алгоритмов']

    # Лекторы
    lecturer1 = Lecturer('Смирнов', 'Алексей')
    lecturer2 = Lecturer('Козлова', 'Елена')
    lecturer1.courses_attached += ['Python', 'Git']
    lecturer2.courses_attached += ['Python', 'Java']

    # Рецензенты
    reviewer1 = Reviewer('Васильев', 'Дмитрий')
    reviewer2 = Reviewer('Соколова', 'Ольга')
    reviewer1.courses_attached += ['Python', 'Git']
    reviewer2.courses_attached += ['Python', 'Java']

    print('✓ Студенты, лекторы, рецензенты созданы\n')

    # 2. Вызываем все созданные методы
    print('--- Вызываем методы ---')

    # Рецензенты ставят оценки студентам
    print('Рецензенты оценивают домашние задания:')
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Git', 7)
    reviewer2.rate_hw(student2, 'Python', 10)
    reviewer2.rate_hw(student2, 'Python', 9)
    reviewer2.rate_hw(student2, 'Java', 8)
    print('✓ Оценки студентам выставлены')

    # Студенты оценивают лекторов
    print('\nСтуденты оценивают лекторов:')
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 10)
    student1.rate_lecture(lecturer1, 'Git', 8)
    student2.rate_lecture(lecturer2, 'Python', 7)
    student2.rate_lecture(lecturer2, 'Python', 8)
    student2.rate_lecture(lecturer2, 'Java', 9)
    print('✓ Оценки лекторам выставлены')

    # Вывод __str__ для всех
    print('\n--- Вывод информации через __str__ ---')
    print('Рецензент 1:', reviewer1)
    print('Рецензент 2:', reviewer2)
    print('Лектор 1:', lecturer1)
    print('Лектор 2:', lecturer2)
    print('Студент 1:', student1)
    print('Студент 2:', student2)

    # Сравнение лекторов
    print('\n--- Сравнение лекторов ---')
    print(f'{lecturer1.first_name} > {lecturer2.first_name}: {lecturer1 > lecturer2}')
    print(f'{lecturer1.first_name} < {lecturer2.first_name}: {lecturer1 < lecturer2}')
    print(f'{lecturer1.first_name} == {lecturer2.first_name}: {lecturer1 == lecturer2}')

    # Сравнение студентов
    print('\n--- Сравнение студентов ---')
    print(f'{student1.first_name} > {student2.first_name}: {student1 > student2}')
    print(f'{student1.first_name} < {student2.first_name}: {student1 < student2}')
    print(f'{student1.first_name} == {student2.first_name}: {student1 == student2}')

    # 3. Проверка новых функций подсчёта средних оценок
    print('\n=== ПРОВЕРКА НОВЫХ ФУНКЦИЙ ===')

    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    # Средняя оценка студентов по курсам
    print('\n--- Средние оценки студентов по курсам ---')
    for course in ['Python', 'Git', 'Java']:
        avg = average_grade_for_course_students(students_list, course)
        print(f'Курс {course}: {avg}')

    # Средняя оценка лекторов по курсам
    print('\n--- Средние оценки лекторов по курсам ---')
    for course in ['Python', 'Git', 'Java']:
        avg = average_grade_for_course_lecturers(lecturers_list, course)
        print(f'Курс {course}: {avg}')


if __name__ == '__main__':
    main()