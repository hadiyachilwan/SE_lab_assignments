# student_grades.py

class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student, grade):
        """Add a grade for a student."""
        if student in self.grades:
            self.grades[student].append(grade)
        else:
            self.grades[student] = [grade]

    def get_grades(self, student):
        """Return the grades of a specific student."""
        return self.grades.get(student, [])

    def get_average_grade(self, student):
        """Return the average grade of a student."""
        grades = self.get_grades(student)
        if grades:
            return sum(grades) / len(grades)
        return 0.0

    def get_all_students(self):
        """Return a list of all student names."""
        return list(self.grades.keys())
