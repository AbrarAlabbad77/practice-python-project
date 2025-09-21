import unittest
from student.student import Student


class testStuedent(unittest.TestCase):
    def test_create_stuent_object(self):
        new_student = Student('Abrar')
        self.assertEqual(new_student.name, 'Abrar')
    