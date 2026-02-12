class Human:
    def __init__(self, first_name: str, last_name: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Student(Human):
    def __init__(self, first_name: str, last_name: str, gender: str):
        super().__init__(first_name, last_name, gender)
        self.grades = {}

    def add_grade(self, subject: str, grade: int):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self) -> float:
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def __str__(self) -> str:
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка: {self.average_grade():.1f}"

    def __lt__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Human):
    def __init__(self, first_name: str, last_name: str, gender: str):
        super().__init__(first_name, last_name, gender)

    def add_grade(self, student: Student, subject: str, grade: int):
        if isinstance(student, Student):
            student.add_grade(subject, grade)

    def __str__(self) -> str:
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"


class Lecturer(Human):
    def __init__(self, first_name: str, last_name: str, gender: str):
        super().__init__(first_name, last_name, gender)
        self.grades = {}

    def add_grade(self, subject: str, grade: int):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self) -> float:
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)

    def __str__(self) -> str:
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {self.average_grade():.1f}"

    def __lt__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


def average_students_grade(students: list, subject: str) -> float:
    """Подсчет средней оценки за ДЗ по конкретному предмету для списка студентов"""
    total = 0
    count = 0
    for student in students:
        if isinstance(student, Student) and subject in student.grades:
            total += sum(student.grades[subject])
            count += len(student.grades[subject])
    return total / count if count > 0 else 0.0


def average_lecturers_grade(lecturers: list, subject: str) -> float:
    """Подсчет средней оценки за лекции по конкретному предмету для списка лекторов"""
    total = 0
    count = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and subject in lecturer.grades:
            total += sum(lecturer.grades[subject])
            count += len(lecturer.grades[subject])
    return total / count if count > 0 else 0.0

if __name__ == "__main__":
    # Создаем список студентов
    students = []

    s1 = Student("Иван", "Иванов", "мужской")
    s1.add_grade("Математика", 5)
    s1.add_grade("Математика", 4)
    students.append(s1)

    s2 = Student("Мария", "Петрова", "женский")
    s2.add_grade("Математика", 4)
    s2.add_grade("Математика", 4)
    students.append(s2)

    # Создаем список лекторов
    lecturers = []

    l1 = Lecturer("Анна", "Смирнова", "женский")
    l1.add_grade("Математика", 5)
    l1.add_grade("Математика", 4)
    lecturers.append(l1)

    l2 = Lecturer("Ольга", "Козлова", "женский")
    l2.add_grade("Математика", 4)
    l2.add_grade("Математика", 4)
    lecturers.append(l2)

    # Вывод студентов
    for student in students:
        print(student)
        print()

    # Вывод лекторов
    for lecturer in lecturers:
        print(lecturer)
        print()

    # Подсчет средних оценок
    print(f"Средняя оценка студентов по Математике: {average_students_grade(students, 'Математика'):.1f}")
    print(f"Средняя оценка лекторов по Математике: {average_lecturers_grade(lecturers, 'Математика'):.1f}")



