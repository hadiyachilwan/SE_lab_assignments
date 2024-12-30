# test_student_grades.py
import unittest
from student_grades import StudentGrades

class TestStudentGrades(unittest.TestCase):

    def setUp(self):
        """Create an instance of StudentGrades before each test."""
        self.sg = StudentGrades()

    def test_add_and_get_grades(self):
        """Test adding and getting grades."""
        self.sg.add_grade('Alice', 90)
        self.sg.add_grade('Alice', 85)
        self.assertEqual(self.sg.get_grades('Alice'), [90, 85])

    def test_get_grades_non_existent_student(self):
        """Test getting grades of a non-existent student."""
        self.assertEqual(self.sg.get_grades('Bob'), [])

    def test_get_average_grade(self):
        """Test calculating the average grade."""
        self.sg.add_grade('Alice', 90)
        self.sg.add_grade('Alice', 80)
        self.assertEqual(self.sg.get_average_grade('Alice'), 85.0)

    def test_get_average_grade_non_existent_student(self):
        """Test calculating average for a non-existent student."""
        self.assertEqual(self.sg.get_average_grade('Bob'), 0.0)

    def test_get_all_students(self):
        """Test getting all students."""
        self.sg.add_grade('Alice', 90)
        self.sg.add_grade('Bob', 85)
        self.assertEqual(set(self.sg.get_all_students()), {'Alice', 'Bob'})

if __name__ == '__main__':
    unittest.main()
