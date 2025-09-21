class Student():
    # store name and list of grade
    def __init__(self, name):
        self.name = name
        self.grades = []

# will run when we run the file directily , but i we doing our modual (in test file) will not work
if __name__ == '__main__':
    student_name = input('Enter the new student name')
    new_student = Student(student_name)
    print(f'welcome{new_student.name}')
    
