class Student:
    def __init__(self, first_name: str, last_name: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
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


class Reviewer:
    def __init__(self, first_name: str, last_name: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def add_grade(self, student: Student, subject: str, grade: int):
        if isinstance(student, Student):
            student.add_grade(subject, grade)

    def __str__(self) -> str:
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"


class Lecturer:
    def __init__(self, first_name: str, last_name: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
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

if __name__ == "__main__":
    # Создаем студента
    student = Student("Иван", "Иванов", "мужской")
    student.add_grade("Математика", 5)
    student.add_grade("Математика", 4)
    student.add_grade("Физика", 5)
    print(student)
    print()

    # Создаем ревьюера
    reviewer = Reviewer("Петр", "Петров", "мужской")
    print(reviewer)
    print()

    # Создаем лектора
    lecturer = Lecturer("Анна", "Смирнова", "женский")
    lecturer.add_grade("Математика", 5)
    lecturer.add_grade("Математика", 4)
    print(lecturer)



