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

if __name__ == "__main__":
    # Создаем студентов
    student1 = Student("Иван", "Иванов", "мужской")
    student1.add_grade("Математика", 5)
    student1.add_grade("Математика", 5)

    student2 = Student("Петр", "Петров", "мужской")
    student2.add_grade("Математика", 3)
    student2.add_grade("Математика", 4)

    # Демонстрация сравнения
    print(student1)
    print()
    print(student2)
    print()
    print(f"student1 > student2: {student1 > student2}")
    print(f"student1 >= student2: {student1 >= student2}")
    print(f"student1 < student2: {student1 < student2}")
    print(f"student1 <= student2: {student1 <= student2}")
    print(f"student1 == student2: {student1 == student2}")
    print()

    # Создаем лекторов
    lecturer1 = Lecturer("Анна", "Смирнова", "женский")
    lecturer1.add_grade("Математика", 5)
    lecturer1.add_grade("Математика", 4)

    lecturer2 = Lecturer("Ольга", "Иванова", "женский")
    lecturer2.add_grade("Математика", 3)
    lecturer2.add_grade("Математика", 4)

    print(lecturer1)
    print()
    print(lecturer2)
    print()
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 >= lecturer2: {lecturer1 >= lecturer2}")

